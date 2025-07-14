#!/usr/bin/env python3
"""
Script to remove unnecessary inline navigation scripts from HTML files.
These scripts are now handled by main.js
"""

import os
import re

def clean_html_file(file_path):
    """Remove unnecessary script blocks from HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Patterns to remove
        patterns = [
            # Hamburger menu toggle script
            r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\)\s*{\s*// Hamburger menu toggle.*?</script>',
            
            # Individual dropdown scripts
            r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\)\s*{\s*// Home Dropdown.*?</script>',
            
            # Mobile dropdown toggle script
            r'<script>\s*document\.querySelectorAll\(\'\.header-bar \.dropdown > \.dropdown-toggle\'\)\.forEach.*?</script>',
            
            # Technologies dropdown script
            r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\)\s*{\s*const technologiesDropdown.*?</script>',
            
            # Technologies mega menu script
            r'<script>\s*// TECHNOLOGIES MEGA MENU SCRIPT.*?</script>',
            
            # Services mega menu script
            r'<script>\s*// SERVICES MEGA MENU SCRIPT.*?</script>',
            
            # Mobile nav close scripts
            r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\)\s*{\s*// Helper to close header bar nav on mobile.*?</script>',
            
            # Standalone mobile nav close script
            r'<script>\s*// Helper to close header bar nav on mobile.*?</script>'
        ]
        
        original_content = content
        
        # Remove each pattern
        for pattern in patterns:
            content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # Clean up extra whitespace
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Cleaned: {file_path}")
            return True
        else:
            print(f"No changes needed: {file_path}")
            return False
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to clean all HTML files"""
    html_files = [
        'servicesXR.html',
        'servicesWordpress.html',
        'servicesWeb.html',
        'servicesVR.html',
        'servicesSoft.html',
        'servicesShopify.html',
        'servicesSeoSearchEngine.html',
        'servicesSaas.html',
        'servicesRedesign.html',
        'servicesNftMarketPlace.html',
        'servicesNftGameDevlopment.html',
        'servicesMR.html',
        'servicesMobile.html',
        'servicesMetaverseSolution.html',
        'servicesMetaverseGameDevlopment.html',
        'servicesLow.html',
        'servicesIosGameDevlopment.html',
        'servicesImmersiveMarketing.html',
        'servicesImmersive.html',
        'servicesGraphics.html',
        'servicesErpDevlopment.html',
        'servicesCrmDevlopment.html',
        'servicesAR.html',
        'servicesAndroidGameDevlopment.html',
        'servicesAIdev.html',
        'servicesBrandIdentity.html',
        'contact.html',
        'blog-inner.html',
        'project-6.html',
        'project-5.html',
        'project-4.html',
        'project-3.html',
        'project-2.html',
        'project-1.html',
        'portfolio-3.html',
        'portfolio-2.html',
        'portfolio-1.html',
        'publication.html',
        'team.html',
        'technologies.html',
        'service.html',
        'services.html',
        'shopify.html',
        'soft.html',
        'wordpress.html',
        'web.html',
        'VR.html',
        'XR.html',
        'MR.html',
        'AR.html',
        'immersive.html',
        'immersiveMarketing.html',
        'iosGameDevlopment.html',
        'metaverseGameDevlopment.html',
        'metaverseSolution.html',
        'mobile.html',
        'nftGameDevlopment.html',
        'nftMarketPlace.html',
        'redesign.html',
        'saas.html',
        'seoSearchEngine.html',
        'technologyMigration.html',
        'low.html',
        'graphics.html',
        'erpDevlopment.html',
        'crmDevlopment.html',
        'androidGameDevlopment.html',
        'AIdev.html',
        'brandIdentity.html',
        'CGI.html',
        'customERP.html',
        'devlopment.html',
        'digitalMarketing.html',
        'about.html',
        'blog.html'
    ]
    
    cleaned_count = 0
    total_files = 0
    
    for html_file in html_files:
        if os.path.exists(html_file):
            total_files += 1
            if clean_html_file(html_file):
                cleaned_count += 1
    
    print(f"\nSummary:")
    print(f"Total files processed: {total_files}")
    print(f"Files cleaned: {cleaned_count}")
    print(f"Files unchanged: {total_files - cleaned_count}")

if __name__ == "__main__":
    main() 