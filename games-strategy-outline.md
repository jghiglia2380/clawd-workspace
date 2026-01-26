# Progressive Financial Life Simulator: Project Brief

## PFL Academy Game-Based Assessment System

**Document Version:** 2.0 (Refined)
**Date:** November 2024
**Purpose:** Comprehensive reference for development partners

---

## Executive Summary

Build a **persistent financial life simulator** where students create and develop a character across an entire semester (18 weeks), making financial decisions that create lasting consequences. Each "game" is a life stage in an ongoing story.

### Key Innovation: Persistence + Progression

Unlike NGPF's disconnected mini-games:
- **One continuous character** built over 18 weeks
- **Decisions persist** across all games/life stages
- **Consequences compound** (good and bad choices create lasting effects)
- **Unique circumstances per student** (natural anti-cheat by design)
- **"Do-over" mechanics** (3 life resets to explore alternative paths)

---

## The Problem We're Solving

**Teacher Feedback:**
> "Students are copying and pasting questions into Google, resulting in everyone getting 100%. I can't tell who actually learned anything."

**Core Issues:**
1. Traditional assessments broken in AI/search era
2. Compliance vs. competency gap
3. Engagement challenges (mid-semester slump)
4. Teacher preparation gap

**Why NGPF Arcade Fails:**
- Disconnected mini-games with no progression
- No persistence between games
- Generic starting conditions
- Easy to share screenshots/answers

---

## Technical Architecture

### 5 Reusable Game Engines

1. **Decision Tree Engine** - Branching scenarios (credit cards, car buying, housing)
2. **Resource Management Engine** - Budget games, time-bound challenges
3. **Calculator/Optimizer Engine** - Loan comparison, investment strategy
4. **Timeline/Projection Engine** - Compound interest, retirement planning
5. **Challenge/Constraint Engine** - Debt payoff, emergency fund building

### Student Financial State (15-20 tracked variables)

- credit_score (300-850)
- savings_balance, checking_balance
- monthly_gross_income, monthly_net_income
- credit_card_balance, credit_card_limit, credit_card_apr
- car_payment, rent_payment
- retirement_balance, investment_portfolio_value
- spending_pattern, payment_history
- life_resets_remaining (default: 3)

---

## Game Progression Example

**Week 1: Character Creation**
- Student creates avatar
- Starting: $500 checking, no credit history, entry-level job

**Game 1: First Paycheck** (after income chapters)
- Decisions: W-4 withholding, budget allocation, savings %
- Creates: Income level, initial savings, spending habits

**Game 3: Credit Card Decision** (after credit chapters)
- Inherits: Income, savings history
- Decisions: Accept offer, spending patterns, payment timing
- Updates: Credit score, debt level

**Game 7: Car Purchase** (after borrowing chapters)
- Inherits: Credit score, savings, monthly income
- Credit score determines APR (poor = 22%, good = 6%)
- Updates: Monthly payment obligations

**Game 10: Housing Decision** (after housing chapters)
- Inherits: Full financial state
- Credit score affects approval chances
- Decisions: Rent, roommates, parents, buy

**Week 18: Life Outcome Review**
- 10-year financial projection
- Compare with peers (anonymized)
- Remaining do-overs to explore alternatives

---

## Anti-Cheat by Design

**Why Screenshots Don't Help:**
- Every student has unique financial state
- Alice: $1,341 saved, 682 credit, $150 car payment
- Bob: $5,120 saved, 745 credit, no car, lives with parents
- Completely different decision options

**Why Google/ChatGPT Don't Help:**
- No "right answer" to copy
- Decisions contextual to individual state
- AI can't play the game for students
- Real-time decision-making under time pressure

---

## Recommended Game Quantity: 12-15 Total

### Distribution (Crescendo, Not Monotony):
- Weeks 1-8: 2-3 games (foundational)
- Weeks 9-14: 5-6 games (peak engagement)
- Weeks 15-18: 4-5 games (synthesis, high-stakes)

### Placement Strategy:
1. **Complexity Gates** (6-8 games) - End of complex topic clusters
2. **Motivation Checkpoints** (3-4 games) - When engagement drops
3. **High-Stakes Decision Training** (4-5 games) - Major life consequences
4. **Sticky Concept Reinforcement** (2-3 games) - Common misunderstandings

---

## Business Model

### Free Tier: Standalone Games
- All 12-15 games accessible
- Generic starting conditions
- NO persistence between games
- NO teacher analytics
- NO LMS integration

### Paid Tier: Progressive Assessment System ($34/student)
- Full curriculum (45-69 chapters)
- Character persistence
- 3 life resets
- Teacher analytics dashboard
- Automated grading + LMS integration
- State-specific personalization
- Spanish language

---

## Development Phases

### Phase 1: MVP (6-8 weeks) - ~$4,000
- Core state management
- 2 game engines (Decision Tree + Resource Management)
- 3 complete games
- One state configuration
- Basic teacher dashboard

### Phase 2: Beta (8-10 weeks) - ~$5,000
- Remaining 3 game engines
- 9-12 additional games
- Do-over mechanic
- Enhanced analytics
- 5 state configurations

### Phase 3: Pilot (Spring 2025) - ~$3,000
- Production deployment
- 10+ state configurations
- Spanish UI
- Teacher training

### Phase 4: Scale (Fall 2025+)
- All 62 state configurations
- Full Spanish curriculum
- Advanced analytics
- Mobile optimization

---

## Current Status

- ✅ 69 chapters complete (English)
- ✅ 69 chapters translated (Spanish)
- ✅ 62 state configurations available
- 🔄 Backend integration in progress
- ⏳ Game system development ready to begin

---

## Competitive Advantage vs NGPF

| Feature | NGPF | PFL Academy |
|---------|------|-------------|
| Price | Free | $26-34/student |
| Games | 12 disconnected | 12-15 progressive |
| Persistence | None | Full semester |
| State customization | None | 62 configs, 86+ variables |
| Anti-cheat | Weak | By design |
| LMS integration | No | Yes (Canvas, Schoology) |
| Teacher analytics | Basic | Advanced |
| Spanish | Limited | Full curriculum |

---

## 80-100 Universal Financial Concepts

Games test concepts, not chapters:

**Income & Budgeting:** gross_vs_net_income, payroll_taxes, budget_allocation, needs_vs_wants, emergency_fund

**Credit & Debt:** credit_score_factors, apr_calculation, minimum_payment, credit_utilization, debt_payoff_strategies

**Saving & Investing:** compound_interest, rule_of_72, time_value_of_money, risk_return_tradeoff, diversification

**Housing:** rent_vs_buy_analysis, affordability_calculation, mortgage_basics

**Insurance & Risk:** risk_assessment, coverage_decisions, premium_deductible_tradeoff

**Taxes:** progressive_taxation, tax_bracket_calculation, deductions_vs_credits
