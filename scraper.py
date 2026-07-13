import os

def create_website_files():
    """إنشاء SmartNote Pro - Legendary Edition"""
    
    os.makedirs("www", exist_ok=True)
    
    html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SmartNote Pro | Legendary</title>
    <style>
        :root {
            --bg: #000;
            --surface: #080808;
            --card: #0d0d0d;
            --border: #1a1a1a;
            --gold: #c9a84c;
            --gold-light: #e2c97e;
            --gold-dark: #8b7300;
            --gold-glow: rgba(201,168,76,0.5);
            --text: #e0d5c0;
            --text-dim: #6b6355;
            --red: #ff6b6b;
            --blue: #6ba3ff;
            --green: #6bff8e;
            --purple: #c26bff;
            --orange: #ffb74d;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            background: #000;
            color: var(--text);
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 12px;
            background-image: 
                radial-gradient(ellipse at 30% 0%, rgba(201,168,76,0.06) 0%, transparent 50%),
                radial-gradient(ellipse at 70% 100%, rgba(201,168,76,0.04) 0%, transparent 50%);
            overflow-x: hidden;
        }

        .bg-particles {
            position: fixed; inset: 0; pointer-events: none; z-index: 0;
        }

        .particle {
            position: absolute; background: var(--gold);
            border-radius: 50%; opacity: 0;
            animation: floatUp 5s ease-in infinite;
        }

        @keyframes floatUp {
            0% { transform: translateY(100vh) scale(0); opacity: 0; }
            10% { opacity: 0.5; }
            90% { opacity: 0.1; }
            100% { transform: translateY(-10vh) scale(2.5); opacity: 0; }
        }

        .app { width: 100%; max-width: 500px; position: relative; z-index: 1; }

        /* Header */
        .header { text-align: center; margin-bottom: 20px; position: relative; }

        .crown-icon {
            position: absolute; top: -26px; left: 50%; transform: translateX(-50%);
            font-size: 24px; animation: crownFloat 2s ease-in-out infinite;
        }

        @keyframes crownFloat {
            0%, 100% { transform: translateX(-50%) translateY(0) rotate(0deg); }
            25% { transform: translateX(-50%) translateY(-4px) rotate(-4deg); }
            75% { transform: translateX(-50%) translateY(-2px) rotate(4deg); }
        }

        .logo-container {
            width: 80px; height: 80px; margin: 0 auto 12px; position: relative;
        }

        .logo-ring {
            position: absolute; inset: -8px;
            border: 1px solid rgba(201,168,76,0.2); border-radius: 50%;
            animation: outerSpin 20s linear infinite;
        }

        .logo-ring2 {
            position: absolute; inset: -4px;
            border: 1px dashed rgba(201,168,76,0.15); border-radius: 50%;
            animation: outerSpin 15s linear infinite reverse;
        }

        @keyframes outerSpin { to { transform: rotate(360deg); } }

        .logo-core {
            width: 100%; height: 100%;
            background: radial-gradient(circle at 40% 40%, #1a1a0a, #000);
            border: 2px solid var(--gold); border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 34px;
            box-shadow: 0 0 40px var(--gold-glow), 0 0 80px rgba(201,168,76,0.1);
            animation: logoPulse 3s ease-in-out infinite;
            position: relative; z-index: 3;
        }

        @keyframes logoPulse {
            0%, 100% { box-shadow: 0 0 40px var(--gold-glow), 0 0 80px rgba(201,168,76,0.1); }
            50% { box-shadow: 0 0 60px var(--gold-glow), 0 0 110px rgba(201,168,76,0.2); }
        }

        .title {
            font-size: 30px; font-weight: 900; letter-spacing: 4px;
            background: linear-gradient(180deg, var(--gold-light) 0%, var(--gold) 40%, var(--gold-dark) 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            background-clip: text;
            filter: drop-shadow(0 0 20px rgba(201,168,76,0.4));
        }

        .title-glow {
            width: 70px; height: 1px; margin: 4px auto 0;
            background: linear-gradient(90deg, transparent, var(--gold), var(--gold-light), var(--gold), transparent);
            filter: blur(1px);
        }

        .subtitle {
            font-size: 9px; color: var(--text-dim);
            letter-spacing: 5px; text-transform: uppercase; margin-top: 2px;
        }

        .divider {
            display: flex; align-items: center; gap: 8px;
            margin: 12px auto; width: fit-content;
        }
        .divider-line {
            width: 20px; height: 1px;
            background: linear-gradient(90deg, transparent, var(--gold));
        }
        .divider-line:last-child { background: linear-gradient(90deg, var(--gold), transparent); }
        .divider-diamond { font-size: 7px; color: var(--gold); }

        /* Card */
        .card {
            background: var(--card); border: 1px solid var(--border);
            border-radius: 20px; overflow: hidden;
            box-shadow: 0 30px 60px rgba(0,0,0,0.7), 0 0 0 1px rgba(255,255,255,0.02) inset;
            position: relative;
        }

        .card::before {
            content: ''; position: absolute; top: 0; left: 15%; right: 15%; height: 1px;
            background: linear-gradient(90deg, transparent, rgba(201,168,76,0.5), var(--gold), rgba(201,168,76,0.5), transparent);
            z-index: 2;
        }

        /* Notes List */
        .notes-section {
            border-bottom: 1px solid var(--border);
            max-height: 180px;
            overflow-y: auto;
            background: rgba(0,0,0,0.3);
        }

        .notes-section::-webkit-scrollbar { width: 3px; }
        .notes-section::-webkit-scrollbar-thumb { background: #222; border-radius: 3px; }

        .notes-header {
            display: flex; justify-content: space-between; align-items: center;
            padding: 12px 16px; border-bottom: 1px solid rgba(255,255,255,0.03);
            position: sticky; top: 0; background: var(--card); z-index: 1;
        }

        .notes-title {
            font-size: 9px; letter-spacing: 4px; color: var(--text-dim); text-transform: uppercase;
        }

        .btn-new {
            padding: 7px 14px; background: linear-gradient(135deg, rgba(201,168,76,0.15), rgba(201,168,76,0.05));
            border: 1px solid var(--gold); color: var(--gold); cursor: pointer;
            border-radius: 20px; font-size: 10px; font-weight: 700;
            letter-spacing: 1px; transition: all 0.3s; font-family: inherit;
        }

        .btn-new:hover {
            background: rgba(201,168,76,0.25); box-shadow: 0 0 15px var(--gold-glow);
            transform: translateY(-1px);
        }

        .search-bar {
            padding: 8px 16px; display: flex; gap: 6px;
            position: sticky; top: 42px; background: var(--card); z-index: 1;
        }

        .search-input {
            flex: 1; padding: 8px 12px; background: var(--bg);
            border: 1px solid var(--border); color: var(--text);
            font-size: 10px; border-radius: 20px; font-family: inherit; outline: none;
            transition: all 0.3s;
        }

        .search-input:focus { border-color: var(--gold); box-shadow: 0 0 0 2px rgba(201,168,76,0.1); }

        .note-item {
            padding: 12px 16px; cursor: pointer;
            border-bottom: 1px solid rgba(255,255,255,0.02);
            transition: all 0.3s; display: flex;
            justify-content: space-between; align-items: center;
        }

        .note-item:hover { background: rgba(255,255,255,0.02); }
        .note-item.active {
            background: linear-gradient(90deg, rgba(201,168,76,0.08), transparent);
            border-left: 3px solid var(--gold);
        }

        .note-info { flex: 1; min-width: 0; }
        .note-title-text {
            font-size: 12px; font-weight: 600;
            white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
            display: flex; align-items: center; gap: 6px;
        }

        .note-color { width: 10px; height: 10px; border-radius: 50%; display: inline-block; flex-shrink: 0; }

        .note-meta {
            font-size: 8px; color: var(--text-dim); letter-spacing: 1px;
            display: flex; gap: 8px; margin-top: 3px;
        }

        .btn-delete {
            background: none; border: none; color: #ff4444;
            cursor: pointer; font-size: 14px; opacity: 0.3;
            transition: 0.3s; padding: 4px 8px;
        }

        .note-item:hover .btn-delete { opacity: 0.7; }
        .btn-delete:hover { opacity: 1; }

        /* Editor */
        .editor-section { padding: 16px; }

        .editor-header {
            display: flex; justify-content: space-between;
            align-items: center; margin-bottom: 10px; gap: 8px;
        }

        .title-input {
            flex: 1; padding: 10px 14px; background: var(--bg);
            border: 1px solid var(--border); color: var(--text);
            font-size: 15px; font-weight: 700; border-radius: 10px;
            font-family: inherit; outline: none; transition: all 0.3s;
        }

        .title-input:focus { border-color: var(--gold); box-shadow: 0 0 0 3px rgba(201,168,76,0.1); }

        .color-picker { display: flex; gap: 4px; }
        .color-dot {
            width: 22px; height: 22px; border-radius: 50%; cursor: pointer;
            border: 2px solid transparent; transition: all 0.3s;
        }

        .color-dot:hover { transform: scale(1.15); }
        .color-dot.active { border-color: #fff; transform: scale(1.2); box-shadow: 0 0 10px currentColor; }

        /* Toolbar */
        .toolbar {
            display: flex; gap: 3px; margin-bottom: 10px;
            flex-wrap: wrap; padding: 6px; background: var(--bg);
            border-radius: 10px; border: 1px solid var(--border);
        }

        .tool-btn {
            width: 30px; height: 30px; background: transparent;
            border: none; color: var(--text-dim); cursor: pointer;
            border-radius: 6px; font-size: 13px;
            display: flex; align-items: center; justify-content: center;
            transition: all 0.3s;
        }

        .tool-btn:hover { background: rgba(255,255,255,0.05); color: var(--text); }
        .tool-btn:active { background: rgba(201,168,76,0.2); color: var(--gold); }

        /* Textarea */
        .editor-textarea {
            width: 100%; height: 220px; padding: 16px;
            background: var(--bg); border: 1px solid var(--border);
            color: var(--text); font-size: 13px; border-radius: 12px;
            font-family: 'JetBrains Mono', 'Courier New', monospace;
            line-height: 1.8; resize: vertical; outline: none;
            transition: all 0.4s;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3) inset;
        }

        .editor-textarea:focus {
            border-color: var(--gold);
            box-shadow: 0 0 0 4px var(--gold-glow), 0 4px 15px rgba(0,0,0,0.3) inset;
        }

        .editor-textarea::placeholder { color: #2a2520; }

        /* Stats */
        .stats-bar {
            display: grid; grid-template-columns: repeat(4, 1fr);
            gap: 6px; margin: 10px 0;
        }

        .stat {
            text-align: center; padding: 8px 4px;
            background: var(--bg); border: 1px solid var(--border);
            border-radius: 8px; font-size: 8px; color: var(--text-dim);
            letter-spacing: 1px; text-transform: uppercase;
        }

        .stat-val { font-size: 15px; font-weight: 700; color: var(--gold); display: block; margin-bottom: 2px; }

        /* Actions */
        .action-buttons {
            display: grid; grid-template-columns: repeat(3, 1fr); gap: 5px;
        }

        .btn-action {
            padding: 10px 6px; background: var(--bg);
            border: 1px solid var(--border); color: var(--text-dim);
            cursor: pointer; border-radius: 8px;
            font-size: 8px; font-weight: 700; letter-spacing: 1px;
            transition: all 0.3s; font-family: inherit; text-align: center;
            text-transform: uppercase;
        }

        .btn-action:hover { border-color: var(--gold); color: var(--gold); background: rgba(201,168,76,0.05); }

        .btn-save {
            background: linear-gradient(135deg, var(--gold-dark), var(--gold), var(--gold-light));
            color: #000; border: none; font-weight: 900; grid-column: span 2;
            box-shadow: 0 4px 15px var(--gold-glow); font-size: 10px; letter-spacing: 2px;
        }

        .btn-save:hover { box-shadow: 0 8px 25px var(--gold-glow); transform: translateY(-1px); }

        /* Modal */
        .modal-overlay {
            display: none; position: fixed; inset: 0;
            background: rgba(0,0,0,0.95); z-index: 100;
            align-items: center; justify-content: center;
            backdrop-filter: blur(10px);
        }

        .modal-overlay.show { display: flex; }

        .modal {
            background: var(--card); border: 1px solid var(--border);
            border-radius: 20px; padding: 24px; width: 90%; max-width: 340px;
            box-shadow: 0 30px 60px rgba(0,0,0,0.8);
            animation: modalIn 0.3s ease;
        }

        @keyframes modalIn {
            from { opacity: 0; transform: scale(0.9) translateY(20px); }
            to { opacity: 1; transform: scale(1) translateY(0); }
        }

        .modal h3 { text-align: center; margin-bottom: 16px; color: var(--gold); letter-spacing: 3px; font-size: 14px; }
        .modal-btn {
            width: 100%; padding: 12px; margin-bottom: 6px;
            background: var(--bg); border: 1px solid var(--border);
            color: var(--text); cursor: pointer; border-radius: 10px;
            font-size: 12px; transition: 0.3s; font-family: inherit;
        }

        .modal-btn:hover { border-color: var(--gold); color: var(--gold); background: rgba(201,168,76,0.05); }
        .modal-close {
            width: 100%; padding: 10px; background: transparent;
            border: 1px solid #333; color: #666; cursor: pointer;
            border-radius: 10px; font-size: 11px; margin-top: 8px; font-family: inherit;
        }

        /* Toast */
        .toast {
            position: fixed; bottom: 30px; left: 50%;
            transform: translateX(-50%) translateY(120px);
            background: #0a0a0a; border: 1px solid var(--gold);
            color: var(--gold); padding: 12px 24px;
            border-radius: 30px; font-size: 11px; letter-spacing: 2px;
            z-index: 200; transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 15px 40px rgba(0,0,0,0.9), 0 0 30px var(--gold-glow);
        }

        .toast.show { transform: translateX(-50%) translateY(0); }

        .footer {
            text-align: center; margin-top: 16px;
            font-size: 8px; color: #111; letter-spacing: 3px;
        }
        .footer span { color: var(--gold); }
        .footer .dot { color: var(--gold); margin: 0 5px; }

        .empty-state {
            text-align: center; padding: 30px 20px; color: #111;
        }
        .empty-state .icon { font-size: 40px; display: block; margin-bottom: 8px; opacity: 0.4; }
        .empty-state .text { font-size: 10px; letter-spacing: 2px; text-transform: uppercase; }
    </style>
</head>
<body>
    <!-- Particles -->
    <div class="bg-particles" id="particles"></div>

    <div class="app">
        <!-- Header -->
        <div class="header">
            <div class="crown-icon">👑</div>
            <div class="logo-container">
                <div class="logo-ring"></div>
                <div class="logo-ring2"></div>
                <div class="logo-core">📝</div>
            </div>
            <h1 class="title">SMARTNOTE PRO</h1>
            <div class="title-glow"></div>
            <p class="subtitle">✦ Legendary Edition ✦</p>
            <div class="divider">
                <span class="divider-line"></span>
                <span class="divider-diamond">◆</span>
                <span class="divider-line"></span>
            </div>
        </div>

        <!-- Card -->
        <div class="card">
            <!-- Notes List -->
            <div class="notes-section" id="notesListSection">
                <div class="notes-header">
                    <span class="notes-title">✦ My Notes</span>
                    <button class="btn-new" onclick="newNote()">+ New Note</button>
                </div>
                <div class="search-bar">
                    <input type="text" class="search-input" placeholder="🔍 Search notes..." id="searchInput" oninput="renderNotesList()">
                </div>
                <div id="notesList">
                    <div class="empty-state">
                        <span class="icon">📭</span>
                        <span class="text">No notes yet</span>
                    </div>
                </div>
            </div>

            <!-- Editor -->
            <div class="editor-section">
                <div class="editor-header">
                    <input type="text" class="title-input" placeholder="Note title..." id="noteTitle" oninput="autoSave()">
                    <div class="color-picker">
                        <span class="color-dot active" style="background:#c9a84c" data-color="#c9a84c" onclick="setColor('#c9a84c', this)"></span>
                        <span class="color-dot" style="background:#ff6b6b" data-color="#ff6b6b" onclick="setColor('#ff6b6b', this)"></span>
                        <span class="color-dot" style="background:#6ba3ff" data-color="#6ba3ff" onclick="setColor('#6ba3ff', this)"></span>
                        <span class="color-dot" style="background:#6bff8e" data-color="#6bff8e" onclick="setColor('#6bff8e', this)"></span>
                        <span class="color-dot" style="background:#c26bff" data-color="#c26bff" onclick="setColor('#c26bff', this)"></span>
                    </div>
                </div>

                <div class="toolbar">
                    <button class="tool-btn" onclick="formatText('bold')"><b>B</b></button>
                    <button class="tool-btn" onclick="formatText('italic')"><i>I</i></button>
                    <button class="tool-btn" onclick="formatText('underline')"><u>U</u></button>
                    <button class="tool-btn" onclick="formatText('h1')">H1</button>
                    <button class="tool-btn" onclick="formatText('h2')">H2</button>
                    <button class="tool-btn" onclick="formatText('h3')">H3</button>
                    <button class="tool-btn" onclick="formatText('list')">•≡</button>
                    <button class="tool-btn" onclick="formatText('numlist')">1.</button>
                    <button class="tool-btn" onclick="formatText('quote')">❝</button>
                    <button class="tool-btn" onclick="formatText('code')">&lt;/&gt;</button>
                    <button class="tool-btn" onclick="formatText('link')">🔗</button>
                    <button class="tool-btn" onclick="formatText('divider')">—</button>
                </div>

                <textarea class="editor-textarea" id="noteContent" placeholder="Start writing your masterpiece..." oninput="autoSave()"></textarea>

                <div class="stats-bar">
                    <div class="stat"><span class="stat-val" id="wordCount">0</span>Words</div>
                    <div class="stat"><span class="stat-val" id="charCount">0</span>Chars</div>
                    <div class="stat"><span class="stat-val" id="lineCount">0</span>Lines</div>
                    <div class="stat"><span class="stat-val" id="readTime">0s</span>Read</div>
                </div>

                <div class="action-buttons">
                    <button class="btn-action btn-save" onclick="saveNote()">💾 Save Note</button>
                    <button class="btn-action" onclick="showExportModal()">📥 Export</button>
                    <button class="btn-action" onclick="exportNote('txt')">📄 TXT</button>
                    <button class="btn-action" onclick="exportNote('md')">📝 MD</button>
                    <button class="btn-action" onclick="exportNote('html')">🌐 HTML</button>
                    <button class="btn-action" onclick="exportNote('pdf')">📑 PDF</button>
                    <button class="btn-action" onclick="exportNote('json')">💾 JSON</button>
                    <button class="btn-action" onclick="shareNote()">📤 Share</button>
                    <button class="btn-action" onclick="duplicateNote()">📋 Duplicate</button>
                </div>
            </div>
        </div>

        <p class="footer">
            <span>◆</span> Powered by <span>SmartNote Pro</span> <span class="dot">•</span> Local Storage <span>◆</span>
        </p>
    </div>

    <!-- Toast -->
    <div class="toast" id="toast"></div>

    <!-- Export Modal -->
    <div class="modal-overlay" id="exportModal">
        <div class="modal">
            <h3>📥 Export Note As</h3>
            <button class="modal-btn" onclick="doExport('txt')">📄 Plain Text (.txt)</button>
            <button class="modal-btn" onclick="doExport('md')">📝 Markdown (.md)</button>
            <button class="modal-btn" onclick="doExport('html')">🌐 HTML (.html)</button>
            <button class="modal-btn" onclick="doExport('pdf')">📑 PDF (.pdf)</button>
            <button class="modal-btn" onclick="doExport('json')">💾 JSON Backup (.json)</button>
            <button class="modal-close" onclick="closeExport()">✕ Cancel</button>
        </div>
    </div>

    <script>
        // ==================== PARTICLES ====================
        (function() {
            const c = document.getElementById('particles');
            for (let i = 0; i < 12; i++) {
                const p = document.createElement('div');
                p.className = 'particle';
                p.style.left = Math.random() * 100 + '%';
                const s = Math.random() * 2 + 1;
                p.style.width = s + 'px'; p.style.height = s + 'px';
                p.style.animationDuration = (Math.random() * 7 + 4) + 's';
                p.style.animationDelay = (Math.random() * 5) + 's';
                c.appendChild(p);
            }
        })();

        // ==================== STATE ====================
        let notes = JSON.parse(localStorage.getItem('smartnotes') || '[]');
        let currentNoteId = null;
        let currentColor = '#c9a84c';
        let saveTimeout = null;

        function loadNotes() { notes = JSON.parse(localStorage.getItem('smartnotes') || '[]'); }
        function saveNotes() { localStorage.setItem('smartnotes', JSON.stringify(notes)); }

        // ==================== NOTES LIST ====================
        function renderNotesList() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const list = document.getElementById('notesList');
            
            const filtered = notes.filter(n => 
                n.title.toLowerCase().includes(searchTerm) || 
                n.content.toLowerCase().includes(searchTerm)
            );

            if (filtered.length === 0) {
                list.innerHTML = '<div class="empty-state"><span class="icon">📭</span><span class="text">No notes found</span></div>';
                return;
            }

            list.innerHTML = filtered.map(n => {
                const preview = n.content.substring(0, 50).replace(/\n/g, ' ') + (n.content.length > 50 ? '...' : '');
                return `
                <div class="note-item ${n.id === currentNoteId ? 'active' : ''}" onclick="openNote('${n.id}')">
                    <div class="note-info">
                        <div class="note-title-text">
                            <span class="note-color" style="background:${n.color || '#c9a84c'}"></span>
                            ${n.title || 'Untitled'}
                        </div>
                        <div class="note-meta">
                            <span>${n.date || ''}</span>
                            <span>${n.content.split(/\s+/).filter(w=>w).length} words</span>
                        </div>
                    </div>
                    <button class="btn-delete" onclick="event.stopPropagation(); deleteNote('${n.id}')">🗑</button>
                </div>
            `}).join('');
        }

        function newNote() {
            const note = {
                id: Date.now().toString(),
                title: '',
                content: '',
                color: '#c9a84c',
                date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
            };
            notes.unshift(note);
            saveNotes();
            openNote(note.id);
            renderNotesList();
            showToast('✨ New note created');
        }

        function openNote(id) {
            const note = notes.find(n => n.id === id);
            if (!note) return;
            
            currentNoteId = id;
            document.getElementById('noteTitle').value = note.title;
            document.getElementById('noteContent').value = note.content;
            currentColor = note.color;
            
            document.querySelectorAll('.color-dot').forEach(d => {
                d.classList.toggle('active', d.dataset.color === note.color);
            });
            
            updateStats();
            renderNotesList();
        }

        function setColor(color, el) {
            currentColor = color;
            document.querySelectorAll('.color-dot').forEach(d => d.classList.remove('active'));
            el.classList.add('active');
            autoSave();
        }

        function autoSave() {
            if (!currentNoteId) return;
            clearTimeout(saveTimeout);
            saveTimeout = setTimeout(() => {
                const note = notes.find(n => n.id === currentNoteId);
                if (!note) return;
                note.title = document.getElementById('noteTitle').value;
                note.content = document.getElementById('noteContent').value;
                note.color = currentColor;
                note.date = new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
                saveNotes();
                updateStats();
            }, 500);
        }

        function saveNote() {
            clearTimeout(saveTimeout);
            autoSave();
            renderNotesList();
            showToast('✅ Note saved!');
        }

        function deleteNote(id) {
            if (!confirm('Delete this note permanently?')) return;
            notes = notes.filter(n => n.id !== id);
            saveNotes();
            if (currentNoteId === id) {
                currentNoteId = null;
                document.getElementById('noteTitle').value = '';
                document.getElementById('noteContent').value = '';
            }
            renderNotesList();
            showToast('🗑 Note deleted');
        }

        function duplicateNote() {
            if (!currentNoteId) return showToast('⚠️ No note selected');
            const original = notes.find(n => n.id === currentNoteId);
            if (!original) return;
            const duplicate = {
                ...original, id: Date.now().toString(),
                title: original.title + ' (Copy)',
                date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
            };
            notes.unshift(duplicate);
            saveNotes();
            openNote(duplicate.id);
            renderNotesList();
            showToast('📋 Note duplicated');
        }

        // ==================== FORMATTING ====================
        function formatText(type) {
            const ta = document.getElementById('noteContent');
            const start = ta.selectionStart;
            const end = ta.selectionEnd;
            const text = ta.value;
            const selected = text.substring(start, end);
            let replacement = '';
            
            const formats = {
                bold: `**${selected || 'bold text'}**`,
                italic: `*${selected || 'italic text'}*`,
                underline: `__${selected || 'underlined text'}__`,
                h1: `\n# ${selected || 'Heading 1'}\n`,
                h2: `\n## ${selected || 'Heading 2'}\n`,
                h3: `\n### ${selected || 'Heading 3'}\n`,
                list: `\n- ${selected || 'List item'}`,
                numlist: `\n1. ${selected || 'List item'}`,
                quote: `\n> ${selected || 'Quote'}\n`,
                code: '`' + (selected || 'code') + '`',
                link: `[${selected || 'link text'}](url)`,
                divider: `\n---\n`
            };
            
            replacement = formats[type] || '';
            ta.value = text.substring(0, start) + replacement + text.substring(end);
            ta.focus();
            ta.setSelectionRange(start + replacement.length, start + replacement.length);
            autoSave();
        }

        // ==================== STATS ====================
        function updateStats() {
            const content = document.getElementById('noteContent').value;
            const words = content.trim() ? content.trim().split(/\s+/).length : 0;
            const chars = content.length;
            const lines = content ? content.split('\n').length : 0;
            const readTime = Math.max(1, Math.ceil(words / 200 * 60));
            
            document.getElementById('wordCount').textContent = words;
            document.getElementById('charCount').textContent = chars;
            document.getElementById('lineCount').textContent = lines;
            document.getElementById('readTime').textContent = readTime + 's';
        }

        // ==================== EXPORT ====================
        function showExportModal() {
            if (!currentNoteId) return showToast('⚠️ No note selected');
            document.getElementById('exportModal').classList.add('show');
        }

        function closeExport() {
            document.getElementById('exportModal').classList.remove('show');
        }

        function exportNote(format) {
            if (!currentNoteId) return showToast('⚠️ No note selected');
            const note = notes.find(n => n.id === currentNoteId);
            if (!note) return;
            doExport(format, note);
        }

        function doExport(format, noteOverride) {
            const note = noteOverride || notes.find(n => n.id === currentNoteId);
            if (!note) return;
            
            let content = '', filename = '', mimeType = 'text/plain';
            
            switch(format) {
                case 'txt':
                    content = `${note.title}\n${'='.repeat(note.title.length || 1)}\n\n${note.content}`;
                    filename = (note.title || 'note') + '.txt';
                    break;
                case 'md':
                    content = `# ${note.title}\n\n${note.content}`;
                    filename = (note.title || 'note') + '.md';
                    break;
                case 'html':
                    content = `<!DOCTYPE html>\n<html>\n<head><meta charset="UTF-8"><title>${note.title}</title><style>body{font-family:Arial;max-width:800px;margin:40px auto;padding:20px;color:#333;background:#fff}h1{color:#c9a84c;border-bottom:2px solid #c9a84c}</style></head>\n<body>\n<h1>${note.title}</h1>\n${note.content.split('\n').map(l => '<p>' + l + '</p>').join('\n')}\n</body>\n</html>`;
                    filename = (note.title || 'note') + '.html';
                    mimeType = 'text/html';
                    break;
                case 'pdf':
                    content = `<!DOCTYPE html>\n<html>\n<head><title>${note.title}</title><style>body{font-family:Arial;padding:30px;color:#222;line-height:1.8}h1{color:#c9a84c;border-bottom:2px solid #c9a84c;padding-bottom:10px}</style></head>\n<body>\n<h1>${note.title}</h1>\n${note.content.split('\n').map(l => '<p>' + l + '</p>').join('\n')}\n</body>\n</html>`;
                    filename = (note.title || 'note') + '.pdf';
                    mimeType = 'application/pdf';
                    break;
                case 'json':
                    content = JSON.stringify({note: note, exportedAt: new Date().toISOString()}, null, 2);
                    filename = (note.title || 'backup') + '.json';
                    mimeType = 'application/json';
                    break;
            }
            
            const blob = new Blob([content], { type: mimeType });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url; a.download = filename.replace(/[^a-z0-9]/gi, '_').toLowerCase();
            document.body.appendChild(a); a.click(); document.body.removeChild(a);
            URL.revokeObjectURL(url);
            
            closeExport();
            showToast('📥 Exported as ' + format.toUpperCase());
        }

        // ==================== SHARE ====================
        async function shareNote() {
            if (!currentNoteId) return showToast('⚠️ No note selected');
            const note = notes.find(n => n.id === currentNoteId);
            if (!note) return;
            
            if (navigator.share) {
                try {
                    await navigator.share({ title: note.title, text: note.content.substring(0, 500) });
                } catch (err) {}
            } else {
                try {
                    await navigator.clipboard.writeText(note.content);
                    showToast('📋 Copied to clipboard!');
                } catch(e) {
                    showToast('⚠️ Could not copy');
                }
            }
        }

        // ==================== TOAST ====================
        function showToast(msg) {
            const toast = document.getElementById('toast');
            toast.textContent = msg;
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2500);
        }

        // ==================== KEYBOARD SHORTCUTS ====================
        document.addEventListener('keydown', function(e) {
            if ((e.ctrlKey || e.metaKey) && e.key === 's') {
                e.preventDefault();
                saveNote();
            }
            if ((e.ctrlKey || e.metaKey) && e.key === 'n') {
                e.preventDefault();
                newNote();
            }
        });

        // ==================== INIT ====================
        loadNotes();
        renderNotesList();
        if (notes.length > 0) openNote(notes[0].id);
        updateStats();
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("╔══════════════════════════════════════════╗")
    print("║  👑 SmartNote Pro - Legendary Edition  ║")
    print("║  📝 تم الإنشاء بنجاح                   ║")
    print("╚══════════════════════════════════════════╝")
    print(f"📁 www/index.html")
    print(f"💾 حجم الملف: {os.path.getsize('www/index.html')/1024:.1f} KB")
    print("")
    print("✨ المميزات الأسطورية:")
    print("  👑 تاج متحرك + جسيمات ذهبية")
    print("  💫 حلقات دائرية حول الشعار")
    print("  🎨 5 ألوان للتمييز")
    print("  🔧 12 أداة تنسيق (B, I, U, H1, H2, H3, List, NumList, Quote, Code, Link, Divider)")
    print("  💾 Auto-Save مع تأخير 500ms")
    print("  📊 إحصائيات: كلمات، أحرف، أسطر، وقت قراءة")
    print("  📥 5 صيغ تصدير (TXT, MD, HTML, PDF, JSON)")
    print("  📤 مشاركة + نسخ")
    print("  📋 نسخ الملاحظة")
    print("  🔍 بحث في الملاحظات")
    print("  ⌨️ اختصارات كيبورد (Ctrl+S, Ctrl+N)")
    print("  📱 معاينة المحتوى في القائمة")
    print("  🔔 Toast notifications فاخرة")

if __name__ == "__main__":
    create_website_files()
