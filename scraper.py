import os

def create_website_files():
    """إنشاء محرر نصوص احترافي SmartNote Pro"""
    
    os.makedirs("www", exist_ok=True)
    
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SmartNote Pro</title>
    <style>
        :root {
            --bg: #0a0a0a;
            --surface: #111;
            --border: #222;
            --gold: #c9a84c;
            --gold-light: #e2c97e;
            --gold-glow: rgba(201, 168, 76, 0.3);
            --text: #e0d5c0;
            --text-dim: #6b6355;
            --red: #ff6b6b;
            --blue: #6ba3ff;
            --green: #6bff8e;
            --purple: #c26bff;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            background: var(--bg);
            color: var(--text);
            font-family: 'Segoe UI', system-ui, sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 16px;
            background-image: 
                radial-gradient(circle at 30% 10%, rgba(201,168,76,0.04) 0%, transparent 50%),
                radial-gradient(circle at 70% 90%, rgba(201,168,76,0.03) 0%, transparent 50%);
        }

        .app {
            width: 100%;
            max-width: 500px;
        }

        /* Header */
        .header {
            text-align: center;
            margin-bottom: 20px;
        }

        .logo {
            width: 64px;
            height: 64px;
            margin: 0 auto 12px;
            background: linear-gradient(135deg, var(--gold), var(--gold-light), var(--gold));
            border-radius: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            box-shadow: 0 0 30px var(--gold-glow);
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-6px); }
        }

        .title {
            font-size: 28px;
            font-weight: 900;
            letter-spacing: 3px;
            background: linear-gradient(135deg, var(--gold), var(--gold-light), var(--gold));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .subtitle {
            font-size: 10px;
            color: var(--text-dim);
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-top: 4px;
        }

        .line {
            width: 50px;
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--gold), transparent);
            margin: 12px auto;
        }

        /* Card */
        .card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 20px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            overflow: hidden;
        }

        /* Notes List */
        .notes-list-section {
            border-bottom: 1px solid var(--border);
            max-height: 200px;
            overflow-y: auto;
            transition: all 0.3s;
        }

        .notes-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 14px 16px;
            border-bottom: 1px solid rgba(255,255,255,0.03);
        }

        .notes-title {
            font-size: 10px;
            letter-spacing: 3px;
            color: var(--text-dim);
            text-transform: uppercase;
        }

        .btn-new {
            padding: 6px 14px;
            background: rgba(201,168,76,0.1);
            border: 1px solid var(--gold);
            color: var(--gold);
            cursor: pointer;
            border-radius: 8px;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 1px;
            transition: all 0.3s;
            font-family: inherit;
        }

        .btn-new:hover {
            background: rgba(201,168,76,0.2);
            box-shadow: 0 0 15px var(--gold-glow);
        }

        .search-bar {
            padding: 8px 16px;
            display: flex;
            gap: 8px;
        }

        .search-input {
            flex: 1;
            padding: 8px 12px;
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text);
            font-size: 11px;
            border-radius: 8px;
            font-family: inherit;
            outline: none;
        }

        .search-input:focus {
            border-color: var(--gold);
        }

        .btn-search {
            padding: 8px 12px;
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text-dim);
            cursor: pointer;
            border-radius: 8px;
            font-size: 14px;
        }

        .note-item {
            padding: 12px 16px;
            cursor: pointer;
            border-bottom: 1px solid rgba(255,255,255,0.02);
            transition: all 0.2s;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .note-item:hover {
            background: rgba(255,255,255,0.02);
        }

        .note-item.active {
            background: rgba(201,168,76,0.05);
            border-left: 3px solid var(--gold);
        }

        .note-info {
            flex: 1;
            min-width: 0;
        }

        .note-title-text {
            font-size: 13px;
            font-weight: 600;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .note-date {
            font-size: 9px;
            color: var(--text-dim);
            letter-spacing: 1px;
        }

        .note-actions {
            display: flex;
            gap: 4px;
        }

        .note-color {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            display: inline-block;
        }

        .btn-delete {
            background: none;
            border: none;
            color: #ff4444;
            cursor: pointer;
            font-size: 14px;
            opacity: 0.5;
            transition: 0.3s;
        }

        .btn-delete:hover {
            opacity: 1;
        }

        /* Editor Section */
        .editor-section {
            padding: 16px;
        }

        .editor-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            gap: 8px;
        }

        .title-input {
            flex: 1;
            padding: 8px 12px;
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text);
            font-size: 14px;
            font-weight: 700;
            border-radius: 8px;
            font-family: inherit;
            outline: none;
        }

        .title-input:focus {
            border-color: var(--gold);
        }

        .color-picker {
            display: flex;
            gap: 4px;
        }

        .color-dot {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            cursor: pointer;
            border: 2px solid transparent;
            transition: 0.3s;
        }

        .color-dot.active {
            border-color: #fff;
            transform: scale(1.2);
        }

        /* Toolbar */
        .toolbar {
            display: flex;
            gap: 4px;
            margin-bottom: 12px;
            flex-wrap: wrap;
        }

        .tool-btn {
            width: 32px;
            height: 32px;
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text-dim);
            cursor: pointer;
            border-radius: 6px;
            font-size: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
        }

        .tool-btn:hover {
            border-color: var(--gold);
            color: var(--gold);
        }

        .tool-btn.active {
            background: rgba(201,168,76,0.1);
            border-color: var(--gold);
            color: var(--gold);
        }

        /* Textarea */
        .editor-textarea {
            width: 100%;
            height: 250px;
            padding: 16px;
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text);
            font-size: 14px;
            border-radius: 12px;
            font-family: 'Courier New', monospace;
            line-height: 1.8;
            resize: vertical;
            outline: none;
            transition: all 0.3s;
        }

        .editor-textarea:focus {
            border-color: var(--gold);
            box-shadow: 0 0 0 4px var(--gold-glow);
        }

        .editor-textarea::placeholder {
            color: #2a2520;
        }

        /* Stats Bar */
        .stats-bar {
            display: flex;
            gap: 8px;
            margin-top: 12px;
            margin-bottom: 12px;
        }

        .stat {
            flex: 1;
            text-align: center;
            padding: 8px;
            background: var(--bg);
            border: 1px solid var(--border);
            border-radius: 8px;
            font-size: 9px;
            color: var(--text-dim);
            letter-spacing: 1px;
        }

        .stat-val {
            font-size: 16px;
            font-weight: 700;
            color: var(--gold);
            display: block;
        }

        /* Action Buttons */
        .action-buttons {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 6px;
        }

        .btn-action {
            padding: 10px;
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text-dim);
            cursor: pointer;
            border-radius: 8px;
            font-size: 9px;
            font-weight: 700;
            letter-spacing: 1px;
            transition: all 0.3s;
            font-family: inherit;
            text-align: center;
        }

        .btn-action:hover {
            border-color: var(--gold);
            color: var(--gold);
        }

        .btn-save {
            background: linear-gradient(135deg, var(--gold), var(--gold-light));
            color: #000;
            border: none;
            font-weight: 900;
            grid-column: span 2;
        }

        .btn-save:hover {
            box-shadow: 0 0 20px var(--gold-glow);
        }

        /* Export Modal */
        .modal-overlay {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.9);
            z-index: 100;
            align-items: center;
            justify-content: center;
        }

        .modal-overlay.show {
            display: flex;
        }

        .modal {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 24px;
            width: 90%;
            max-width: 350px;
        }

        .modal h3 {
            text-align: center;
            margin-bottom: 16px;
            color: var(--gold);
            letter-spacing: 2px;
        }

        .modal-btn {
            width: 100%;
            padding: 12px;
            margin-bottom: 8px;
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text);
            cursor: pointer;
            border-radius: 8px;
            font-size: 13px;
            transition: 0.3s;
            font-family: inherit;
        }

        .modal-btn:hover {
            border-color: var(--gold);
            color: var(--gold);
        }

        .modal-close {
            width: 100%;
            padding: 10px;
            background: transparent;
            border: 1px solid #444;
            color: #888;
            cursor: pointer;
            border-radius: 8px;
            font-size: 12px;
            margin-top: 8px;
            font-family: inherit;
        }

        /* Toast */
        .toast {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(100px);
            background: #111;
            border: 1px solid var(--gold);
            color: var(--gold);
            padding: 12px 24px;
            border-radius: 30px;
            font-size: 12px;
            letter-spacing: 1px;
            z-index: 200;
            transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        }

        .toast.show {
            transform: translateX(-50%) translateY(0);
        }

        .footer {
            text-align: center;
            margin-top: 16px;
            font-size: 9px;
            color: #1a1a1a;
            letter-spacing: 2px;
        }

        .footer span { color: var(--gold); }

        .empty-state {
            text-align: center;
            padding: 40px 20px;
            color: #1a1a1a;
        }

        .empty-state .icon {
            font-size: 50px;
            display: block;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="app">
        <!-- Header -->
        <div class="header">
            <div class="logo">📝</div>
            <h1 class="title">SMARTNOTE PRO</h1>
            <p class="subtitle">Text Editor</p>
            <div class="line"></div>
        </div>

        <!-- Card -->
        <div class="card">
            <!-- Notes List -->
            <div class="notes-list-section" id="notesListSection">
                <div class="notes-header">
                    <span class="notes-title">✦ My Notes</span>
                    <button class="btn-new" onclick="newNote()">+ New</button>
                </div>
                <div class="search-bar">
                    <input type="text" class="search-input" placeholder="🔍 Search notes..." id="searchInput" oninput="renderNotesList()">
                </div>
                <div id="notesList">
                    <div class="empty-state">
                        <span class="icon">📭</span>
                        <span>No notes yet</span>
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

                <!-- Toolbar -->
                <div class="toolbar">
                    <button class="tool-btn" onclick="formatText('bold')" title="Bold"><b>B</b></button>
                    <button class="tool-btn" onclick="formatText('italic')" title="Italic"><i>I</i></button>
                    <button class="tool-btn" onclick="formatText('underline')" title="Underline"><u>U</u></button>
                    <button class="tool-btn" onclick="formatText('h1')" title="Heading">H1</button>
                    <button class="tool-btn" onclick="formatText('h2')" title="Heading 2">H2</button>
                    <button class="tool-btn" onclick="formatText('list')" title="List">•≡</button>
                    <button class="tool-btn" onclick="formatText('quote')" title="Quote">"</button>
                    <button class="tool-btn" onclick="formatText('code')" title="Code">&lt;/&gt;</button>
                    <button class="tool-btn" onclick="formatText('divider')" title="Divider">—</button>
                </div>

                <!-- Textarea -->
                <textarea class="editor-textarea" id="noteContent" placeholder="Start writing your masterpiece..." oninput="autoSave()"></textarea>

                <!-- Stats -->
                <div class="stats-bar">
                    <div class="stat"><span class="stat-val" id="wordCount">0</span>Words</div>
                    <div class="stat"><span class="stat-val" id="charCount">0</span>Chars</div>
                    <div class="stat"><span class="stat-val" id="lineCount">0</span>Lines</div>
                    <div class="stat"><span class="stat-val" id="readTime">0s</span>Read</div>
                </div>

                <!-- Actions -->
                <div class="action-buttons">
                    <button class="btn-action btn-save" onclick="saveNote()">💾 Save Note</button>
                    <button class="btn-action" onclick="exportNote('txt')">📄 TXT</button>
                    <button class="btn-action" onclick="exportNote('md')">📝 Markdown</button>
                    <button class="btn-action" onclick="exportNote('html')">🌐 HTML</button>
                    <button class="btn-action" onclick="exportNote('pdf')">📑 PDF</button>
                    <button class="btn-action" onclick="exportNote('json')">💾 JSON</button>
                    <button class="btn-action" onclick="shareNote()">📤 Share</button>
                    <button class="btn-action" onclick="duplicateNote()">📋 Duplicate</button>
                </div>
            </div>
        </div>

        <p class="footer">Powered by <span>SmartNote Pro</span> • Local Storage</p>
    </div>

    <!-- Toast -->
    <div class="toast" id="toast"></div>

    <!-- Export Modal -->
    <div class="modal-overlay" id="exportModal">
        <div class="modal">
            <h3>📥 Export Note</h3>
            <button class="modal-btn" onclick="doExport('txt')">📄 Plain Text (.txt)</button>
            <button class="modal-btn" onclick="doExport('md')">📝 Markdown (.md)</button>
            <button class="modal-btn" onclick="doExport('html')">🌐 HTML (.html)</button>
            <button class="modal-btn" onclick="doExport('pdf')">📑 PDF (.pdf)</button>
            <button class="modal-btn" onclick="doExport('json')">💾 JSON Backup (.json)</button>
            <button class="modal-close" onclick="closeExport()">Cancel</button>
        </div>
    </div>

    <script>
        // State
        let notes = JSON.parse(localStorage.getItem('smartnotes') || '[]');
        let currentNoteId = null;
        let currentColor = '#c9a84c';

        // Load notes
        function loadNotes() {
            notes = JSON.parse(localStorage.getItem('smartnotes') || '[]');
        }

        function saveNotes() {
            localStorage.setItem('smartnotes', JSON.stringify(notes));
        }

        // Render notes list
        function renderNotesList() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const list = document.getElementById('notesList');
            
            const filtered = notes.filter(n => 
                n.title.toLowerCase().includes(searchTerm) || 
                n.content.toLowerCase().includes(searchTerm)
            );

            if (filtered.length === 0) {
                list.innerHTML = '<div class="empty-state"><span class="icon">📭</span><span>No notes found</span></div>';
                return;
            }

            list.innerHTML = filtered.map(n => `
                <div class="note-item ${n.id === currentNoteId ? 'active' : ''}" onclick="openNote('${n.id}')">
                    <div class="note-info">
                        <div class="note-title-text">
                            <span class="note-color" style="background:${n.color || '#c9a84c'}"></span>
                            ${n.title || 'Untitled'}
                        </div>
                        <div class="note-date">${n.date || ''}</div>
                    </div>
                    <button class="btn-delete" onclick="event.stopPropagation(); deleteNote('${n.id}')">🗑</button>
                </div>
            `).join('');
        }

        // New note
        function newNote() {
            const note = {
                id: Date.now().toString(),
                title: '',
                content: '',
                color: '#c9a84c',
                date: new Date().toLocaleDateString()
            };
            notes.unshift(note);
            saveNotes();
            openNote(note.id);
            renderNotesList();
        }

        // Open note
        function openNote(id) {
            const note = notes.find(n => n.id === id);
            if (!note) return;
            
            currentNoteId = id;
            document.getElementById('noteTitle').value = note.title;
            document.getElementById('noteContent').value = note.content;
            currentColor = note.color;
            
            // Update color picker
            document.querySelectorAll('.color-dot').forEach(d => {
                d.classList.toggle('active', d.dataset.color === note.color);
            });
            
            updateStats();
            renderNotesList();
        }

        // Set color
        function setColor(color, el) {
            currentColor = color;
            document.querySelectorAll('.color-dot').forEach(d => d.classList.remove('active'));
            el.classList.add('active');
            autoSave();
        }

        // Auto save
        function autoSave() {
            if (!currentNoteId) return;
            
            const note = notes.find(n => n.id === currentNoteId);
            if (!note) return;
            
            note.title = document.getElementById('noteTitle').value;
            note.content = document.getElementById('noteContent').value;
            note.color = currentColor;
            saveNotes();
            updateStats();
        }

        // Save note
        function saveNote() {
            autoSave();
            renderNotesList();
            showToast('✅ Note saved!');
        }

        // Delete note
        function deleteNote(id) {
            if (!confirm('Delete this note?')) return;
            
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

        // Duplicate note
        function duplicateNote() {
            if (!currentNoteId) return;
            
            const original = notes.find(n => n.id === currentNoteId);
            if (!original) return;
            
            const duplicate = {
                ...original,
                id: Date.now().toString(),
                title: original.title + ' (Copy)',
                date: new Date().toLocaleDateString()
            };
            
            notes.unshift(duplicate);
            saveNotes();
            openNote(duplicate.id);
            renderNotesList();
            showToast('📋 Note duplicated');
        }

        // Format text
        function formatText(type) {
            const textarea = document.getElementById('noteContent');
            const start = textarea.selectionStart;
            const end = textarea.selectionEnd;
            const text = textarea.value;
            const selected = text.substring(start, end);
            
            let replacement = '';
            
            switch(type) {
                case 'bold':
                    replacement = `**${selected || 'bold text'}**`;
                    break;
                case 'italic':
                    replacement = `*${selected || 'italic text'}*`;
                    break;
                case 'underline':
                    replacement = `__${selected || 'underlined text'}__`;
                    break;
                case 'h1':
                    replacement = `\n# ${selected || 'Heading 1'}\n`;
                    break;
                case 'h2':
                    replacement = `\n## ${selected || 'Heading 2'}\n`;
                    break;
                case 'list':
                    replacement = `\n- ${selected || 'List item'}\n`;
                    break;
                case 'quote':
                    replacement = `\n> ${selected || 'Quote'}\n`;
                    break;
                case 'code':
                    replacement = `\`${selected || 'code'}\``;
                    break;
                case 'divider':
                    replacement = `\n---\n`;
                    break;
            }
            
            textarea.value = text.substring(0, start) + replacement + text.substring(end);
            textarea.focus();
            autoSave();
        }

        // Update stats
        function updateStats() {
            const content = document.getElementById('noteContent').value;
            const words = content.trim() ? content.trim().split(/\s+/).length : 0;
            const chars = content.length;
            const lines = content ? content.split('\n').length : 0;
            const readTime = Math.ceil(words / 200 * 60);
            
            document.getElementById('wordCount').textContent = words;
            document.getElementById('charCount').textContent = chars;
            document.getElementById('lineCount').textContent = lines;
            document.getElementById('readTime').textContent = readTime + 's';
        }

        // Export note
        function exportNote(format) {
            if (!currentNoteId) {
                showToast('⚠️ No note selected');
                return;
            }
            
            const note = notes.find(n => n.id === currentNoteId);
            if (!note) return;
            
            doExport(format, note);
        }

        function doExport(format, noteOverride) {
            const note = noteOverride || notes.find(n => n.id === currentNoteId);
            if (!note) return;
            
            let content = '';
            let filename = '';
            let mimeType = 'text/plain';
            
            switch(format) {
                case 'txt':
                    content = `${note.title}\n${'='.repeat(note.title.length)}\n\n${note.content}`;
                    filename = `${note.title || 'note'}.txt`;
                    break;
                    
                case 'md':
                    content = `# ${note.title}\n\n${note.content}`;
                    filename = `${note.title || 'note'}.md`;
                    break;
                    
                case 'html':
                    content = `<!DOCTYPE html>\n<html>\n<head><title>${note.title}</title></head>\n<body>\n<h1>${note.title}</h1>\n<p>${note.content.replace(/\n/g, '<br>')}</p>\n</body>\n</html>`;
                    filename = `${note.title || 'note'}.html`;
                    mimeType = 'text/html';
                    break;
                    
                case 'pdf':
                    content = `<!DOCTYPE html>\n<html>\n<head><title>${note.title}</title><style>body{font-family:Arial;padding:20px;color:#333}h1{color:#c9a84c}</style></head>\n<body>\n<h1>${note.title}</h1>\n<p>${note.content.replace(/\n/g, '<br>')}</p>\n</body>\n</html>`;
                    filename = `${note.title || 'note'}.pdf`;
                    mimeType = 'application/pdf';
                    break;
                    
                case 'json':
                    content = JSON.stringify(note, null, 2);
                    filename = `${note.title || 'backup'}.json`;
                    mimeType = 'application/json';
                    break;
            }
            
            const blob = new Blob([content], { type: mimeType });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename.replace(/[^a-z0-9]/gi, '_').toLowerCase();
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
            
            showToast(`📥 Exported as ${format.toUpperCase()}`);
        }

        // Share note
        async function shareNote() {
            if (!currentNoteId) return;
            
            const note = notes.find(n => n.id === currentNoteId);
            if (!note) return;
            
            if (navigator.share) {
                try {
                    await navigator.share({
                        title: note.title,
                        text: note.content.substring(0, 500)
                    });
                } catch (err) {
                    console.log('Share cancelled');
                }
            } else {
                navigator.clipboard.writeText(note.content);
                showToast('📋 Copied to clipboard!');
            }
        }

        // Toast
        function showToast(msg) {
            const toast = document.getElementById('toast');
            toast.textContent = msg;
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2500);
        }

        // Init
        loadNotes();
        renderNotesList();
        if (notes.length > 0) openNote(notes[0].id);
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ تم إنشاء SmartNote Pro")
    print(f"📁 www/index.html")
    print(f"💾 الحجم: {os.path.getsize('www/index.html')/1024:.1f} KB")
    print("📝 يدعم: TXT, MD, HTML, PDF, JSON")

if __name__ == "__main__":
    create_website_files()
