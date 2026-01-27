import './index.css'

// PFL Academy exact brand colors
const colors = {
  coverGradient: 'linear-gradient(135deg, #4338ca 0%, #6d28d9 50%, #3730a3 100%)',
  accent: 'rgb(79 70 229)',
  accentLight: 'rgb(99 102 241)',
}

function App() {
  return (
    <div className="min-h-screen bg-zinc-50">
      {/* Header */}
      <header className="fixed top-0 w-full bg-white border-b border-gray-200 z-50">
        <div className="max-w-6xl mx-auto px-6 h-20 flex items-center justify-between">
          <a href="#" className="flex items-center">
            <img 
              src="https://res.cloudinary.com/pflacademy/image/upload/v1747636886/PFL_Academy_logo-Color_qek9en.png" 
              alt="PFL Academy" 
              className="h-10"
            />
          </a>
          <nav className="hidden lg:flex items-center gap-6">
            <a href="#" className="text-gray-700 hover:text-indigo-600 transition-colors text-sm font-medium">Curriculum</a>
            <a href="#" className="text-indigo-600 text-sm font-medium">Showcase</a>
            <a href="#" className="text-gray-700 hover:text-indigo-600 transition-colors text-sm font-medium">Educators</a>
            <button className="bg-indigo-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-indigo-700 transition-colors">
              Sign In
            </button>
          </nav>
        </div>
      </header>

      <div className="h-20" />

      {/* Bento Showcase Section */}
      <section className="py-16 md:py-20">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-12">
            <h1 className="text-3xl md:text-4xl font-bold text-gray-900">
              Real Skills. Real Practice. Real Results.
            </h1>
            <p className="mt-4 text-lg text-gray-600">
              See what students are accomplishing with PFL Academy
            </p>
          </div>

          {/* Bento Grid */}
          <div className="grid grid-cols-4 gap-4 auto-rows-[180px]" style={{ gridAutoRows: 'minmax(180px, auto)' }}>
            
            {/* Featured Video Testimonial - spans 2 cols */}
            <div className="col-span-4 lg:col-span-2 row-span-2 rounded-3xl overflow-hidden text-white p-6 flex flex-col" style={{ background: 'linear-gradient(135deg, #1a1a2e, #16213e)' }}>
              <div className="flex flex-col md:flex-row gap-6 items-center h-full">
                <div className="flex-1 aspect-video bg-white/10 rounded-2xl flex items-center justify-center min-h-[200px]">
                  <div className="w-16 h-16 bg-white/90 rounded-full flex items-center justify-center text-2xl shadow-lg">
                    ▶
                  </div>
                </div>
                <div className="flex-1">
                  <h3 className="text-xl font-bold mb-2">"This actually prepared me for my first interview"</h3>
                  <p className="text-white/80 mb-4">Maria practiced 3 mock interviews before her first real job application. She got the job.</p>
                  <span className="inline-flex items-center gap-2 bg-white/10 px-3 py-1.5 rounded-full text-sm">
                    🎬 Maria M. • Colorado
                  </span>
                </div>
              </div>
            </div>

            {/* Stat: Interviews */}
            <div className="col-span-2 lg:col-span-1 bg-white rounded-3xl p-6 flex flex-col items-center justify-center text-center shadow-sm hover:shadow-md transition-shadow">
              <div className="text-4xl mb-3">🎤</div>
              <div className="text-4xl font-bold text-indigo-600">8,247</div>
              <div className="text-sm text-gray-500 mt-2">Mock Interviews Completed</div>
            </div>

            {/* Stat: Improvement */}
            <div className="col-span-2 lg:col-span-1 rounded-3xl p-6 flex flex-col items-center justify-center text-center shadow-sm hover:shadow-md transition-shadow" style={{ background: 'rgb(238 242 255)' }}>
              <div className="text-4xl mb-3">📈</div>
              <div className="text-4xl font-bold text-indigo-600">89%</div>
              <div className="text-sm text-gray-500 mt-2">Improved After Review</div>
            </div>

            {/* AI Conversation Preview - spans 2 cols */}
            <div className="col-span-4 lg:col-span-2 bg-white rounded-3xl p-6 shadow-sm hover:shadow-md transition-shadow">
              <div className="flex items-center gap-3 mb-4">
                <div className="w-12 h-12 rounded-xl flex items-center justify-center text-2xl" style={{ background: 'linear-gradient(135deg, #dbeafe, #bfdbfe)' }}>
                  🏠
                </div>
                <div>
                  <div className="font-bold text-gray-900">Landlord Negotiation</div>
                  <div className="text-sm text-gray-500">AI Practice Scenario</div>
                </div>
              </div>
              <div className="bg-gray-50 rounded-xl p-4">
                <div className="text-xs uppercase tracking-wide text-gray-400 mb-3">Sample Conversation</div>
                <div className="space-y-2">
                  <div className="flex items-start gap-2">
                    <div className="w-6 h-6 rounded-full bg-indigo-600 text-white flex items-center justify-center text-xs flex-shrink-0">AI</div>
                    <div className="bg-white px-3 py-2 rounded-lg text-sm text-gray-600">"The rent is $1,200/month. First and last due at signing."</div>
                  </div>
                  <div className="flex items-start gap-2">
                    <div className="w-6 h-6 rounded-full bg-indigo-100 text-indigo-600 flex items-center justify-center text-xs flex-shrink-0">S</div>
                    <div className="bg-white px-3 py-2 rounded-lg text-sm text-gray-600">"I've seen similar units at $1,100. Would you consider $1,150 for a 12-month lease?"</div>
                  </div>
                  <div className="flex items-start gap-2">
                    <div className="w-6 h-6 rounded-full bg-indigo-600 text-white flex items-center justify-center text-xs flex-shrink-0">AI</div>
                    <div className="bg-white px-3 py-2 rounded-lg text-sm text-gray-600">"I could do $1,175 if you move in by the 1st."</div>
                  </div>
                </div>
              </div>
            </div>

            {/* Video Testimonial 2 */}
            <div className="col-span-2 lg:col-span-1 rounded-3xl p-5 text-white flex flex-col justify-between" style={{ background: colors.coverGradient }}>
              <div className="aspect-video bg-black/20 rounded-xl flex items-center justify-center mb-3">
                <div className="w-12 h-12 bg-white/90 rounded-full flex items-center justify-center text-xl shadow-lg">▶</div>
              </div>
              <div>
                <h3 className="font-semibold">"I used my budget in real life"</h3>
                <p className="text-sm text-white/80">James T. • Texas</p>
              </div>
            </div>

            {/* Progress Card */}
            <div className="col-span-2 lg:col-span-1 bg-white rounded-3xl p-5 shadow-sm hover:shadow-md transition-shadow">
              <div className="font-bold text-gray-900 mb-4">Skills Practiced This Month</div>
              <div className="space-y-3">
                <div>
                  <div className="flex justify-between text-sm mb-1">
                    <span className="text-gray-600">Mock Interviews</span>
                    <span className="font-semibold text-indigo-600">847</span>
                  </div>
                  <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
                    <div className="h-full rounded-full" style={{ width: '92%', background: `linear-gradient(90deg, ${colors.accent}, ${colors.accentLight})` }} />
                  </div>
                </div>
                <div>
                  <div className="flex justify-between text-sm mb-1">
                    <span className="text-gray-600">Resumes Built</span>
                    <span className="font-semibold text-indigo-600">623</span>
                  </div>
                  <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
                    <div className="h-full rounded-full" style={{ width: '78%', background: `linear-gradient(90deg, ${colors.accent}, ${colors.accentLight})` }} />
                  </div>
                </div>
                <div>
                  <div className="flex justify-between text-sm mb-1">
                    <span className="text-gray-600">Negotiations</span>
                    <span className="font-semibold text-indigo-600">412</span>
                  </div>
                  <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
                    <div className="h-full rounded-full" style={{ width: '65%', background: `linear-gradient(90deg, ${colors.accent}, ${colors.accentLight})` }} />
                  </div>
                </div>
              </div>
            </div>

            {/* Teacher Quote - spans 2 cols */}
            <div className="col-span-4 lg:col-span-2 rounded-3xl p-6 flex flex-col justify-center" style={{ background: 'rgb(238 242 255)' }}>
              <div className="text-3xl text-indigo-600 opacity-50 mb-2">"</div>
              <p className="text-gray-700 italic leading-relaxed mb-4">
                My students don't just learn what a lease is — they negotiate one. They don't just read about interviews — they do them and watch themselves back.
              </p>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-full flex items-center justify-center text-white font-semibold text-sm" style={{ background: colors.coverGradient }}>DM</div>
                <div>
                  <div className="font-semibold text-gray-900">Dianna Martinez</div>
                  <div className="text-sm text-gray-500">Personal Finance Teacher, California</div>
                </div>
              </div>
            </div>

            {/* Stat: Resumes */}
            <div className="col-span-2 lg:col-span-1 bg-white rounded-3xl p-6 flex flex-col items-center justify-center text-center shadow-sm hover:shadow-md transition-shadow">
              <div className="text-4xl mb-3">📄</div>
              <div className="text-4xl font-bold text-indigo-600">6,842</div>
              <div className="text-sm text-gray-500 mt-2">Resumes Built</div>
            </div>

            {/* Stat: Chapters */}
            <div className="col-span-2 lg:col-span-1 rounded-3xl p-6 flex flex-col items-center justify-center text-center shadow-sm hover:shadow-md transition-shadow" style={{ background: 'linear-gradient(135deg, #d1fae5, #a7f3d0)' }}>
              <div className="text-4xl mb-3">📚</div>
              <div className="text-4xl font-bold text-gray-900">45</div>
              <div className="text-sm text-gray-600 mt-2">Life Skill Chapters</div>
            </div>

            {/* Video Testimonial 3 */}
            <div className="col-span-2 lg:col-span-1 rounded-3xl p-5 text-white flex flex-col justify-between" style={{ background: colors.coverGradient }}>
              <div className="aspect-video bg-black/20 rounded-xl flex items-center justify-center mb-3">
                <div className="w-12 h-12 bg-white/90 rounded-full flex items-center justify-center text-xl shadow-lg">▶</div>
              </div>
              <div>
                <h3 className="font-semibold">"I felt ready for adulting"</h3>
                <p className="text-sm text-white/80">Sarah K. • Florida</p>
              </div>
            </div>

            {/* Resume Preview */}
            <div className="col-span-2 lg:col-span-1 bg-white rounded-3xl p-5 shadow-sm hover:shadow-md transition-shadow">
              <div className="flex items-center gap-3 mb-3">
                <div className="w-10 h-10 rounded-xl flex items-center justify-center text-xl" style={{ background: 'linear-gradient(135deg, #d1fae5, #a7f3d0)' }}>
                  📄
                </div>
                <div>
                  <div className="font-bold text-gray-900 text-sm">Resume Building</div>
                  <div className="text-xs text-gray-500">Portfolio-Ready Output</div>
                </div>
              </div>
              <div className="bg-gray-50 rounded-lg p-3 text-xs text-gray-500">
                <div className="font-semibold text-gray-400">████████</div>
                <div className="text-gray-400 mb-2">█████@███.edu • (███) ███-████</div>
                <div><strong>Objective:</strong> Seeking a part-time position...</div>
                <div className="mt-2"><strong>Experience:</strong></div>
                <div>• Volunteer, Local Food Bank</div>
                <div>• Babysitter, Private Families</div>
              </div>
            </div>

            {/* CTA - spans 2 cols */}
            <div className="col-span-4 lg:col-span-2 rounded-3xl p-8 text-white flex flex-col items-center justify-center text-center" style={{ background: colors.coverGradient }}>
              <h3 className="text-xl font-bold mb-2">Prepare Your Students for Real Life</h3>
              <p className="text-white/90 mb-4">45 chapters of hands-on financial literacy. AI-powered practice. Gradebook-ready.</p>
              <a href="#" className="bg-white text-indigo-900 px-6 py-2.5 rounded-lg font-semibold hover:bg-indigo-50 transition-colors">
                Book a Demo →
              </a>
            </div>

          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-8 border-t border-gray-200">
        <div className="max-w-6xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-4">
          <img 
            src="https://res.cloudinary.com/pflacademy/image/upload/v1747636886/PFL_Academy_logo-Color_qek9en.png" 
            alt="PFL Academy" 
            className="h-8"
          />
          <p className="text-gray-500 text-sm">© 2025 PFL Academy. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}

export default App
