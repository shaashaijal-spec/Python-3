# Shawarma & Burgerlak Digital Menu

## Overview

This is a digital restaurant menu application for "Shawarma & Burgerlak" (شاورما و برجرلك), a Middle Eastern fast-food restaurant in Jeddah, Saudi Arabia. The application displays a bilingual (English/Arabic) menu with food items, prices in SAR, calorie information, and variant options. It also includes a QR code generator for customers to scan and view the menu.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Framework
- **Streamlit**: The application uses Streamlit as its web framework for building the interactive menu interface
- Rationale: Streamlit provides rapid development for data-driven applications with minimal frontend code
- The layout is centered and optimized for mobile viewing (customers scanning QR codes)

### Data Structure
- Menu data is stored as a Python dictionary in `main.py` with nested structures for categories, items, and variants
- Each menu item contains: bilingual names (English, Arabic tuple), base price, calorie count, and variant options
- Categories are emoji-prefixed for visual organization

### QR Code Generation
- Uses `qrcode` library with PIL/Pillow for image manipulation
- Supports optional logo embedding in QR center
- Generates framed QR codes with custom text and green border styling
- High error correction (ERROR_CORRECT_H) to accommodate logo overlay

### Bilingual Support
- All menu items support English and Arabic text stored as tuples
- Shop name and contact information available in both languages

## External Dependencies

### Python Libraries
- **streamlit**: Web application framework for the menu display
- **qrcode**: QR code generation
- **Pillow (PIL)**: Image processing for QR code framing and logo embedding

### Assets
- `logo.png`: Restaurant logo file (referenced but may need to be added)

### Contact/Location
- Phone: +966 50 518 9381
- Location: Bryman district, Jeddah, Saudi Arabia