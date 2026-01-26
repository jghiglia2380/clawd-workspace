#!/bin/bash
# Microsoft Graph API Helper for Thomas
# Usage: ./graph-helper.sh <domain> <action> [args...]
# Domains: ss (startup smartup), pfl (pfl academy)
# Actions: users, mail <user> [count], search <user> <query>, read <user> <message_id>, sent <user> [count]

set -e

DOMAIN=$1
ACTION=$2
shift 2

# Load credentials based on domain
if [ "$DOMAIN" == "ss" ]; then
    CLIENT_ID="56393523-351a-4707-a68f-7e7ee76f8c47"
    CLIENT_SECRET="yhs8Q~sPOH--43uAvbzbFCMBFHFjbbb9nHPA6bRN"
    TENANT_ID="00b446d6-0814-41b3-b624-3286a3a2ad80"
    DOMAIN_SUFFIX="startupsmartup.com"
elif [ "$DOMAIN" == "pfl" ]; then
    CLIENT_ID="175a4ecd-3a49-435c-8a1c-3adbad792fc7"
    CLIENT_SECRET="fi~8Q~vg1F53Sd_oZ29zsBUm~lI2X-9vombMebcf"
    TENANT_ID="5d7f0564-1998-4656-98ff-7af9fe20bcc5"
    DOMAIN_SUFFIX="pflacademy.co"
else
    echo "Unknown domain: $DOMAIN (use 'ss' or 'pfl')"
    exit 1
fi

# Get access token
TOKEN=$(curl -s -X POST "https://login.microsoftonline.com/$TENANT_ID/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=$CLIENT_ID" \
  -d "client_secret=$CLIENT_SECRET" \
  -d "scope=https://graph.microsoft.com/.default" \
  -d "grant_type=client_credentials" | jq -r '.access_token')

# Helper function to expand user shorthand
expand_user() {
    local user=$1
    if [[ "$user" != *"@"* ]]; then
        echo "${user}@${DOMAIN_SUFFIX}"
    else
        echo "$user"
    fi
}

case $ACTION in
    users)
        curl -s -H "Authorization: Bearer $TOKEN" \
            "https://graph.microsoft.com/v1.0/users?\$select=displayName,mail,userPrincipalName" | jq '.value[] | {name: .displayName, email: .mail}'
        ;;
    mail)
        USER=$(expand_user $1)
        COUNT=${2:-10}
        curl -s -H "Authorization: Bearer $TOKEN" \
            "https://graph.microsoft.com/v1.0/users/$USER/messages?\$top=$COUNT&\$select=id,subject,from,receivedDateTime,isRead,hasAttachments&\$orderby=receivedDateTime%20desc" | jq '.value[] | {id: .id[0:20], subject, from: .from.emailAddress.address, received: .receivedDateTime, read: .isRead, attachments: .hasAttachments}'
        ;;
    sent)
        USER=$(expand_user $1)
        COUNT=${2:-10}
        curl -s -H "Authorization: Bearer $TOKEN" \
            "https://graph.microsoft.com/v1.0/users/$USER/mailFolders/SentItems/messages?\$top=$COUNT&\$select=id,subject,toRecipients,sentDateTime&\$orderby=sentDateTime%20desc" | jq '.value[] | {id: .id[0:20], subject, to: [.toRecipients[].emailAddress.address], sent: .sentDateTime}'
        ;;
    search)
        USER=$(expand_user $1)
        QUERY=$2
        curl -s -H "Authorization: Bearer $TOKEN" \
            "https://graph.microsoft.com/v1.0/users/$USER/messages?\$search=\"$QUERY\"&\$top=20&\$select=id,subject,from,receivedDateTime,bodyPreview" | jq '.value[] | {id: .id[0:20], subject, from: .from.emailAddress.address, received: .receivedDateTime, preview: .bodyPreview[0:200]}'
        ;;
    read)
        USER=$(expand_user $1)
        MSG_ID=$2
        # Find full message ID if partial
        if [ ${#MSG_ID} -lt 50 ]; then
            FULL_ID=$(curl -s -H "Authorization: Bearer $TOKEN" \
                "https://graph.microsoft.com/v1.0/users/$USER/messages?\$filter=startswith(id,'$MSG_ID')&\$select=id" | jq -r '.value[0].id')
            if [ "$FULL_ID" != "null" ]; then
                MSG_ID=$FULL_ID
            fi
        fi
        curl -s -H "Authorization: Bearer $TOKEN" \
            "https://graph.microsoft.com/v1.0/users/$USER/messages/$MSG_ID?\$select=subject,from,toRecipients,ccRecipients,receivedDateTime,body" | jq '{subject, from: .from.emailAddress, to: [.toRecipients[].emailAddress], cc: [.ccRecipients[]?.emailAddress], received: .receivedDateTime, body: .body.content}'
        ;;
    thread)
        USER=$(expand_user $1)
        QUERY=$2
        curl -s -H "Authorization: Bearer $TOKEN" \
            "https://graph.microsoft.com/v1.0/users/$USER/messages?\$search=\"$QUERY\"&\$top=50&\$select=id,subject,from,toRecipients,receivedDateTime,conversationId&\$orderby=receivedDateTime%20asc" | jq '[.value[] | {id: .id[0:20], subject, from: .from.emailAddress.address, to: [.toRecipients[].emailAddress.address][0], received: .receivedDateTime, thread: .conversationId[0:15]}] | group_by(.thread) | .[] | {thread: .[0].thread, count: length, messages: .}'
        ;;
    *)
        echo "Unknown action: $ACTION"
        echo "Actions: users, mail <user> [count], sent <user> [count], search <user> <query>, read <user> <msg_id>, thread <user> <query>"
        exit 1
        ;;
esac
