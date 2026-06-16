import glob
import re

mobile_css = """
        /* ========== MOBILE MENU & RESPONSIVE FIXES ========== */
        .mobile-menu-btn { display: none; }
        .mobile-menu { display: none; }
        
        @media (max-width: 900px) {
            nav { padding: 1rem 1.5rem !important; }
            .nav-links, .nav-cta { display: none !important; }
            
            .mobile-menu-btn {
                display: flex;
                color: var(--white);
                font-size: 2rem;
                cursor: pointer;
                z-index: 1001;
                align-items: center;
            }
            .mobile-menu {
                position: fixed; top: 0; left: 0; width: 100%; height: 100vh;
                background: rgba(5,5,5,0.98);
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                display: flex; flex-direction: column; align-items: center; justify-content: center;
                gap: 2rem; z-index: 1000;
                transform: translateY(-100%); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            }
            .mobile-menu.active { transform: translateY(0); display: flex; }
            .mobile-menu a { font-size: 1.5rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--white); transition: color 0.3s ease; }
            .mobile-menu a:hover { color: var(--accent-light); }
            
            /* Responsive layout adjustments for mobile */
            section { padding: 4rem 1.5rem !important; }
            .about-suite > div { grid-template-columns: 1fr !important; gap: 3rem !important; }
            .about-suite img { height: 250px !important; }
            .amenities-grid { grid-template-columns: repeat(2, 1fr) !important; gap: 1rem !important; }
            .amenity-item { padding: 1.5rem 1.2rem !important; }
            .gallery-grid { grid-template-columns: 1fr !important; grid-template-rows: auto !important; }
            .gallery-item { height: 220px !important; }
            .gallery-item-main { grid-row: auto !important; }
            .pricing-grid { grid-template-columns: 1fr !important; gap: 1.5rem !important; }
            .pricing-card { padding: 2rem 1.5rem !important; }
            .booking-inner { padding: 0 1rem !important; }
            .booking-actions { flex-direction: column !important; gap: 1rem !important; width: 100% !important; }
            .booking-actions a { width: 100% !important; justify-content: center !important; }
            .footer-mini { padding: 2rem 1.5rem !important; flex-direction: column !important; text-align: center; gap: 1rem !important; }
            .hero-content { padding: 0 1.5rem 4rem !important; }
            .hero-title { font-size: clamp(2.5rem, 8vw, 4rem) !important; }
        }
"""

html_files = glob.glob("suite-*.html")

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if mobile styles are already applied (avoid duplicates)
    if "/* ========== MOBILE MENU & RESPONSIVE FIXES ========== */" in content:
        print(f"Skipping {file_path} - already has mobile styles")
        continue
        
    # We find the closing </style> tag and append mobile CSS before it
    new_content = content.replace("    </style>", mobile_css + "    </style>")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Applied mobile styles to {file_path}")

print("Done.")
