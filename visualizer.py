import os

def generate_svg_screens():
    """Generates 8 simulated detailed SaaS dashboard screens as SVGs"""
    os.makedirs("inputs", exist_ok=True)
    
    # Common UI elements
    base_svg_start = """<svg width="800" height="500" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#0f172a;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#1e293b;stop-opacity:1" />
        </linearGradient>
    </defs>
    <!-- Background -->
    <rect width="800" height="500" fill="url(#grad)"/>
    
    <!-- Sidebar -->
    <rect x="0" y="0" width="180" height="500" fill="#0b0f17" opacity="0.8"/>
    <rect x="20" y="20" width="140" height="30" fill="#00e676" rx="4" opacity="0.1"/>
    <text x="90" y="40" font-family="sans-serif" font-size="16" font-weight="bold" fill="#00e676" text-anchor="middle">Acme Corp</text>
    
    <!-- Sidebar items -->
    <rect x="15" y="80" width="150" height="30" rx="4" fill="#1e293b"/>
    <text x="30" y="100" font-family="sans-serif" font-size="12" fill="#fff">Dashboard</text>
    <text x="30" y="140" font-family="sans-serif" font-size="12" fill="#94a3b8">Analytics</text>
    <text x="30" y="180" font-family="sans-serif" font-size="12" fill="#94a3b8">Reports</text>
    <text x="30" y="220" font-family="sans-serif" font-size="12" fill="#94a3b8">Settings</text>
    
    <!-- Header -->
    <rect x="180" y="0" width="620" height="60" fill="#1e293b" opacity="0.5"/>
    <text x="210" y="35" font-family="sans-serif" font-size="18" font-weight="bold" fill="#fff">System Overview</text>
    <circle cx="760" cy="30" r="15" fill="#334155"/>
"""
    base_svg_end = "</svg>"

    screens = [
        ("01_login", "Login Page", "login"),
        ("02_typing", "Login Page (Typing)", "login_typing"),
        ("03_loading", "Authenticating", "loading"),
        ("04_dashboard", "Main Dashboard", "dashboard"),
        ("05_reports", "Reports View", "reports"),
        ("06_scrolled", "Reports (Scrolled)", "scrolled"),
        ("07_exporting", "Exporting Data", "exporting"),
        ("08_success", "Task Complete", "success")
    ]
    
    for filename, title, state in screens:
        content = ""
        
        if state in ["login", "login_typing"]:
            # Draw a login modal over the background
            content += """
            <rect x="0" y="0" width="800" height="500" fill="#000" opacity="0.6"/>
            <rect x="250" y="120" width="300" height="260" fill="#1e293b" rx="10" stroke="#334155" stroke-width="1"/>
            <text x="400" y="160" font-family="sans-serif" font-size="20" font-weight="bold" fill="#fff" text-anchor="middle">Welcome Back</text>
            
            <text x="280" y="200" font-family="sans-serif" font-size="12" fill="#94a3b8">Email Address</text>
            <rect x="280" y="210" width="240" height="35" rx="4" fill="#0f172a" stroke="#475569" stroke-width="1"/>
            """
            if state == "login":
                content += """
                <text x="290" y="232" font-family="sans-serif" font-size="13" fill="#94a3b8">admin@acme.com</text>
                <rect x="280" y="260" width="240" height="35" rx="4" fill="#0f172a" stroke="#00e676" stroke-width="1"/>
                """
            else: # typing password
                content += """
                <text x="290" y="232" font-family="sans-serif" font-size="13" fill="#fff">admin@acme.com</text>
                <rect x="280" y="260" width="240" height="35" rx="4" fill="#0f172a" stroke="#00e676" stroke-width="1"/>
                <text x="290" y="282" font-family="sans-serif" font-size="13" fill="#fff">••••••••</text>
                <line x1="355" y1="268" x2="355" y2="288" stroke="#00e676" stroke-width="2" class="cursor-blink"/>
                """
                
            content += """
            <text x="280" y="255" font-family="sans-serif" font-size="12" fill="#94a3b8">Password</text>
            <rect x="280" y="315" width="240" height="40" rx="4" fill="#00e676"/>
            <text x="400" y="340" font-family="sans-serif" font-size="14" font-weight="bold" fill="#000" text-anchor="middle">Sign In</text>
            """
            
        elif state == "loading":
            content += """
            <rect x="350" y="200" width="100" height="100" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1"/>
            <circle cx="400" cy="240" r="15" fill="none" stroke="#00e676" stroke-width="3" stroke-dasharray="20 10"/>
            <text x="400" y="280" font-family="sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">Authenticating...</text>
            """
            
        elif state == "dashboard":
            # Draw charts and cards
            content += """
            <rect x="210" y="90" width="170" height="100" rx="8" fill="#1e293b"/>
            <text x="230" y="120" font-family="sans-serif" font-size="13" fill="#94a3b8">Total Revenue</text>
            <text x="230" y="150" font-family="sans-serif" font-size="24" font-weight="bold" fill="#fff">$45,231</text>
            <text x="230" y="170" font-family="sans-serif" font-size="11" fill="#00e676">+20.1% from last month</text>
            
            <rect x="400" y="90" width="170" height="100" rx="8" fill="#1e293b"/>
            <text x="420" y="120" font-family="sans-serif" font-size="13" fill="#94a3b8">Active Users</text>
            <text x="420" y="150" font-family="sans-serif" font-size="24" font-weight="bold" fill="#fff">2,350</text>
            <text x="420" y="170" font-family="sans-serif" font-size="11" fill="#00e676">+180 new today</text>
            
            <rect x="590" y="90" width="170" height="100" rx="8" fill="#1e293b"/>
            <text x="610" y="120" font-family="sans-serif" font-size="13" fill="#94a3b8">System Health</text>
            <text x="610" y="150" font-family="sans-serif" font-size="24" font-weight="bold" fill="#fff">99.9%</text>
            <text x="610" y="170" font-family="sans-serif" font-size="11" fill="#00e676">All systems nominal</text>
            
            <rect x="210" y="210" width="550" height="260" rx="8" fill="#1e293b"/>
            <text x="230" y="240" font-family="sans-serif" font-size="14" font-weight="bold" fill="#fff">Recent Activity</text>
            <!-- Graph lines -->
            <path d="M 230 400 L 300 350 L 380 370 L 460 280 L 540 310 L 620 250 L 700 270" fill="none" stroke="#00e676" stroke-width="3"/>
            <path d="M 230 400 L 300 350 L 380 370 L 460 280 L 540 310 L 620 250 L 700 270 L 700 450 L 230 450 Z" fill="#00e676" opacity="0.1"/>
            """
            
        elif state == "reports":
            content += """
            <!-- Highlight Reports tab -->
            <rect x="15" y="160" width="150" height="30" rx="4" fill="#00e676" opacity="0.2"/>
            
            <rect x="210" y="90" width="550" height="380" rx="8" fill="#1e293b"/>
            <text x="240" y="130" font-family="sans-serif" font-size="18" font-weight="bold" fill="#fff">Q3 Financial Report</text>
            
            <rect x="240" y="160" width="490" height="40" fill="#0f172a" rx="4"/>
            <text x="260" y="185" font-family="sans-serif" font-size="12" fill="#94a3b8">Date | Transaction ID | Amount | Status</text>
            
            <rect x="240" y="210" width="490" height="40" fill="#334155" opacity="0.3" rx="4"/>
            <text x="260" y="235" font-family="sans-serif" font-size="12" fill="#fff">Oct 01 | TR-9938 | $1,250.00 | Completed</text>
            
            <rect x="240" y="260" width="490" height="40" fill="#334155" opacity="0.1" rx="4"/>
            <text x="260" y="285" font-family="sans-serif" font-size="12" fill="#fff">Oct 02 | TR-9939 | $840.00 | Completed</text>
            
            <rect x="240" y="310" width="490" height="40" fill="#334155" opacity="0.3" rx="4"/>
            <text x="260" y="335" font-family="sans-serif" font-size="12" fill="#fff">Oct 03 | TR-9940 | $3,100.00 | Pending</text>
            
            <!-- Scroll indicator -->
            <rect x="740" y="160" width="6" height="60" rx="3" fill="#00e676"/>
            """
            
        elif state == "scrolled":
            content += """
            <rect x="15" y="160" width="150" height="30" rx="4" fill="#00e676" opacity="0.2"/>
            
            <rect x="210" y="90" width="550" height="380" rx="8" fill="#1e293b"/>
            <text x="240" y="130" font-family="sans-serif" font-size="18" font-weight="bold" fill="#fff">Q3 Financial Report (Cont.)</text>
            
            <rect x="240" y="160" width="490" height="40" fill="#0f172a" rx="4"/>
            <text x="260" y="185" font-family="sans-serif" font-size="12" fill="#94a3b8">Date | Transaction ID | Amount | Status</text>
            
            <rect x="240" y="210" width="490" height="40" fill="#334155" opacity="0.3" rx="4"/>
            <text x="260" y="235" font-family="sans-serif" font-size="12" fill="#fff">Oct 30 | TR-9988 | $450.00 | Completed</text>
            
            <rect x="240" y="260" width="490" height="40" fill="#334155" opacity="0.1" rx="4"/>
            <text x="260" y="285" font-family="sans-serif" font-size="12" fill="#fff">Oct 31 | TR-9989 | $2,100.00 | Completed</text>
            
            <text x="240" y="340" font-family="sans-serif" font-size="13" fill="#94a3b8">End of records (45 items)</text>
            
            <rect x="610" y="410" width="120" height="35" rx="4" fill="#00e676"/>
            <text x="670" y="432" font-family="sans-serif" font-size="12" font-weight="bold" fill="#000" text-anchor="middle">Export Data</text>
            
            <!-- Scroll indicator moved down -->
            <rect x="740" y="380" width="6" height="60" rx="3" fill="#00e676"/>
            """
            
        elif state == "exporting":
            content += """
            <rect x="15" y="160" width="150" height="30" rx="4" fill="#00e676" opacity="0.2"/>
            <rect x="210" y="90" width="550" height="380" rx="8" fill="#1e293b"/>
            
            <rect x="0" y="0" width="800" height="500" fill="#000" opacity="0.7"/>
            <rect x="250" y="180" width="300" height="140" fill="#1e293b" rx="10" stroke="#334155" stroke-width="1"/>
            
            <text x="400" y="220" font-family="sans-serif" font-size="16" font-weight="bold" fill="#fff" text-anchor="middle">Preparing Export...</text>
            
            <rect x="280" y="250" width="240" height="10" rx="5" fill="#0f172a"/>
            <rect x="280" y="250" width="150" height="10" rx="5" fill="#00e5ff"/>
            <text x="400" y="285" font-family="sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">62% Complete</text>
            """
            
        elif state == "success":
            content += """
            <rect x="15" y="160" width="150" height="30" rx="4" fill="#00e676" opacity="0.2"/>
            <rect x="210" y="90" width="550" height="380" rx="8" fill="#1e293b"/>
            
            <rect x="0" y="0" width="800" height="500" fill="#000" opacity="0.7"/>
            <rect x="250" y="180" width="300" height="160" fill="#1e293b" rx="10" stroke="#00e676" stroke-width="2"/>
            
            <circle cx="400" cy="220" r="20" fill="#00e676" opacity="0.2"/>
            <path d="M 390 220 L 397 227 L 410 213" fill="none" stroke="#00e676" stroke-width="3" stroke-linecap="round"/>
            
            <text x="400" y="270" font-family="sans-serif" font-size="16" font-weight="bold" fill="#fff" text-anchor="middle">Export Successful!</text>
            <text x="400" y="295" font-family="sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">data_export_q3.csv has been saved.</text>
            """

        svg_code = base_svg_start + content + base_svg_end
        with open(f"inputs/{filename}.svg", "w", encoding="utf-8") as f:
            f.write(svg_code)
            
    return screens

def build_html_dashboard(trajectory):
    """Generates the final HTML visualizer trajectory dashboard with CSS animations"""
    os.makedirs("outputs", exist_ok=True)
    html_path = "outputs/trajectory_dashboard.html"
    
    html_head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jeff-Gemma Animated Visual Trajectory</title>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Space+Grotesk:wght@400;600;700;800&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        :root {
            --bg-main: #0b0f17;
            --bg-card: #141c2b;
            --border-color: rgba(0, 230, 118, 0.18);
            --text-main: #f0f6fc;
            --text-muted: #94a3b8;
            --accent-green: #00e676;
            --accent-cyan: #00e5ff;
            --accent-gold: #ffd600;
        }
        body {
            background-color: var(--bg-main);
            color: var(--text-main);
            font-family: 'Space Grotesk', sans-serif;
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        .header {
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem;
            border: 1px solid var(--border-color);
            border-radius: 16px;
            background: linear-gradient(135deg, rgba(20,28,43,0.9), rgba(11,15,23,0.95));
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            position: relative;
            overflow: hidden;
        }
        .header h1 {
            color: #fff;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        .header h1 span {
            color: var(--accent-green);
        }
        
        .trajectory-timeline {
            display: flex;
            flex-direction: column;
            gap: 2rem;
            max-width: 800px;
            margin: 0 auto;
            position: relative;
        }
        
        /* The connecting line */
        .trajectory-timeline::before {
            content: '';
            position: absolute;
            left: 32px;
            top: 0;
            bottom: 0;
            width: 2px;
            background: rgba(0, 230, 118, 0.2);
            z-index: 0;
        }

        .step-row {
            display: flex;
            gap: 2rem;
            position: relative;
            z-index: 1;
            opacity: 0;
            transform: translateY(20px);
            animation: fadeUpIn 0.6s ease forwards;
        }

        @keyframes fadeUpIn {
            to { opacity: 1; transform: translateY(0); }
        }

        .step-indicator {
            width: 64px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.5rem;
            flex-shrink: 0;
        }
        
        .step-circle {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: var(--bg-card);
            border: 2px solid var(--accent-green);
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'JetBrains Mono', monospace;
            font-weight: bold;
            color: var(--accent-green);
            box-shadow: 0 0 15px rgba(0,230,118,0.2);
        }

        .step-card {
            background: var(--bg-card);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 12px;
            padding: 1.5rem;
            width: 100%;
            position: relative;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        
        .step-card:hover {
            border-color: var(--accent-green);
        }

        .img-container {
            position: relative;
            width: 100%;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.1);
            margin-bottom: 1.5rem;
            background: #000;
        }

        .step-img {
            width: 100%;
            display: block;
        }
        
        /* Simulated Mouse Animation */
        .mouse-cursor {
            position: absolute;
            width: 24px;
            height: 24px;
            z-index: 10;
            opacity: 0;
        }

        @keyframes moveAndClick {
            0% { top: 80%; left: 80%; opacity: 0; }
            20% { top: 80%; left: 80%; opacity: 1; }
            70% { top: var(--target-y); left: var(--target-x); opacity: 1; transform: scale(1); }
            80% { top: var(--target-y); left: var(--target-x); opacity: 1; transform: scale(0.8); }
            90% { top: var(--target-y); left: var(--target-x); opacity: 1; transform: scale(1); }
            100% { top: var(--target-y); left: var(--target-x); opacity: 0; }
        }
        
        /* Simulated Scroll Animation */
        @keyframes scrollDown {
            0% { transform: translateY(0); }
            50% { transform: translateY(-30%); }
            100% { transform: translateY(-30%); }
        }

        .action-title {
            font-size: 1.2rem;
            color: var(--accent-cyan);
            font-weight: bold;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
        }
        
        .stat-box {
            background: rgba(0,0,0,0.4);
            padding: 0.8rem;
            border-radius: 8px;
            border-left: 3px solid var(--accent-gold);
        }
        .stat-box.lat-box { border-left-color: var(--accent-green); }
        
        .stat-value {
            color: #fff;
            font-weight: bold;
            display: block;
            margin-top: 0.3rem;
            font-size: 1.2rem;
        }
        .conf-value { color: var(--accent-gold); }
        .lat-value { color: var(--accent-green); }
        
        /* Typing dot effect */
        .typing-dots {
            display: inline-flex;
            gap: 4px;
        }
        .typing-dots span {
            width: 6px;
            height: 6px;
            background: var(--accent-cyan);
            border-radius: 50%;
            animation: bounce 1.4s infinite ease-in-out both;
        }
        .typing-dots span:nth-child(1) { animation-delay: -0.32s; }
        .typing-dots span:nth-child(2) { animation-delay: -0.16s; }
        @keyframes bounce {
            0%, 80%, 100% { transform: scale(0); }
            40% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Jeff Gemma <span>Live Action Trajectory</span></h1>
        <p>Zero-shot web navigation decisions rendered with simulated execution.</p>
    </div>
    
    <div class="trajectory-timeline">
"""
    
    html_body = ""
    for idx, step in enumerate(trajectory, 1):
        svg_path = f"../inputs/{step['state_id']}.svg"
        action = step['action'].lower()
        
        icon = "mouse-pointer-click"
        cursor_anim = ""
        img_style = ""
        action_display = step['action'].upper()
        
        # Decide animation based on action
        if "type" in action or "password" in action: 
            icon = "keyboard"
            cursor_anim = ""
            action_display += """ <div class="typing-dots"><span></span><span></span><span></span></div>"""
        elif "wait" in action: 
            icon = "hourglass"
        elif "scroll" in action: 
            icon = "arrow-down-square"
            img_style = "animation: scrollDown 4s infinite alternate ease-in-out;"
        elif "complete" in action: 
            icon = "check-circle"
        else: # Click actions
            # Set cursor target based on action
            target_x = "50%"
            target_y = "50%"
            if "login" in action: target_x = "50%"; target_y = "70%"
            elif "reports" in action: target_x = "10%"; target_y = "40%"
            elif "export" in action: target_x = "80%"; target_y = "85%"
            
            cursor_anim = f"""
            <svg class="mouse-cursor" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="--target-x: {target_x}; --target-y: {target_y}; animation: moveAndClick 4s infinite ease-out; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.5));">
                <path d="M3 3l7.07 16.97 2.51-7.39 7.39-2.51L3 3z" fill="#000"/>
            </svg>
            """
            
        html_body += f"""
        <div class="step-row" style="animation-delay: {idx * 0.3}s">
            <div class="step-indicator">
                <div class="step-circle">{idx}</div>
            </div>
            
            <div class="step-card">
                <div class="img-container">
                    <img src="{svg_path}" class="step-img" style="{img_style}" alt="{step['state_title']}">
                    {cursor_anim}
                </div>
                
                <div class="action-title"><i data-lucide="{icon}"></i> {action_display}</div>
                
                <div class="stats-grid">
                    <div class="stat-box">
                        <span style="color: var(--text-muted);">Confidence Score</span>
                        <span class="stat-value conf-value">{step['confidence']*100:.1f}%</span>
                    </div>
                    <div class="stat-box lat-box">
                        <span style="color: var(--text-muted);">Decision Latency</span>
                        <span class="stat-value lat-value">{step['latency_ms']} ms</span>
                    </div>
                </div>
            </div>
        </div>
        """
        
    html_foot = """
    </div>
    <script>lucide.createIcons();</script>
</body>
</html>
"""
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_head + html_body + html_foot)
        
    return html_path
