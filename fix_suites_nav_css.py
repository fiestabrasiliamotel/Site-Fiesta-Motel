import os

site_dir = r"E:\Motel Fiesta\2026\Site novo"
suites = [f for f in os.listdir(site_dir) if f.startswith('suite-') and f.endswith('.html')]

# The CSS for the nav links
nav_css = """
        /* Nav Links */
        .nav-links { display: flex; align-items: center; gap: 2rem; list-style: none; }
        .nav-links a { font-size: 0.85rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--gray); transition: color 0.3s ease; position: relative; }
        .nav-links a::after { content: ''; position: absolute; bottom: -5px; left: 0; width: 0%; height: 1px; background: var(--accent); transition: width 0.3s ease; }
        .nav-links a:hover { color: var(--white); }
        .nav-links a:hover::after { width: 100%; }
        .nav-cta { padding: 0.8rem 1.5rem; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 2px; font-size: 0.75rem; font-weight: 500; letter-spacing: 0.15em; text-transform: uppercase; color: var(--white); transition: all 0.3s ease; }
        .nav-cta:hover { background: var(--white); color: var(--black); }
        @media (max-width: 900px) { .nav-links { display: none; } .nav-cta { display: none; } }
"""

for suite in suites:
    filepath = os.path.join(site_dir, suite)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    if '.nav-links {' not in html:
        # inject before </style>
        html = html.replace('</style>', nav_css + '\n    </style>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
            
print("Injected nav CSS into all suites.")
