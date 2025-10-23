# 📝 Changelog

All notable changes to the LDS Home Assistant Integration will be documented in this file.

## [4.0.0] - 2025-10-23

### 🎉 MAJOR RELEASE - Enhanced Content Platform

#### 🆕 New Features

##### Church Newsroom Integration
- **Added `get_church_newsroom_headlines()`** - Fetches latest church news articles
- **Rich media support** - Includes article images, descriptions, and publication dates
- **Configurable limit** - Get up to 5 latest headlines (default)
- **Full article links** - Direct links to complete news stories

##### Featured Content Integration  
- **Added `get_featured_content()`** - Extracts highlighted church content
- **Comprehensive metadata** - Titles, descriptions, categories (pretitle), and images
- **Curated content** - Church-featured articles, videos, and resources
- **Direct access links** - Links to full featured content

##### Enhanced Data Structure
- **Updated sensor data** - Now includes `newsroom_headlines` and `featured_content` arrays
- **Unified data source** - All content parsed from My Home page JSON data
- **Consistent structure** - Standardized data format across all content types

#### 📰 New Markdown Card Examples

##### Church News Summary Card
- **Full-featured news display** - Headlines with images and descriptions
- **Publication dates** - Shows when articles were published
- **Responsive images** - Properly sized and styled news images
- **Read more links** - Direct access to full articles

##### Featured Content Card
- **Rich content display** - Titles, categories, descriptions, and images
- **Visual appeal** - Professional card layout with featured images
- **Category indicators** - Shows content source/type (pretitle)
- **Learn more links** - Direct access to featured resources

##### Layout Variations
- **Compact News Card** - Single column, condensed layout
- **Featured Content Grid** - Multi-column grid display
- **All-in-One Dashboard** - Combined view with all content types
- **Complete Dashboard View** - Horizontal stack layouts

#### 🔄 Enhanced My Home Page Integration

##### Improved JSON Parsing
- **Comprehensive data extraction** - Newsroom, featured content, prophetic messages
- **Better error handling** - Robust parsing with fallbacks
- **URL validation** - Ensures all links are properly formatted
- **Image optimization** - Proper image URL handling

##### Data Source Migration
- **Scripture parsing** - Now uses My Home page JSON data
- **Quote extraction** - Enhanced quote parsing from multiple sources
- **Unified approach** - Single data source for all content types
- **Real-time updates** - Fresh content from church's My Home page

#### 📚 Comprehensive Documentation Updates

##### Enhanced Card Examples
- **Rich media examples** - Cards with images, styling, and responsive design
- **Multiple layout options** - From compact to full-featured displays
- **Styling guides** - Examples with card-mod integration
- **Copy-paste ready** - Complete YAML configurations

##### Usage Guidelines
- **Best practices** - Recommended card configurations
- **Performance tips** - Optimal settings for different use cases
- **Troubleshooting** - Common issues and solutions
- **Mobile optimization** - Responsive design examples

### 🔧 Technical Improvements

#### Code Organization
- **New methods** - Clean separation of newsroom and featured content logic
- **Enhanced error handling** - Comprehensive exception management
- **Better logging** - Improved debugging capabilities
- **Consistent patterns** - Unified approach across all data fetchers

#### Data Processing
- **JSON parsing optimization** - Efficient extraction from My Home page data
- **URL sanitization** - Proper handling of relative and absolute URLs
- **Image processing** - Optimized image URL handling
- **Content validation** - Ensures data quality and completeness

### ✨ Benefits

#### Enhanced User Experience
- **Richer content** - More diverse church content in dashboards
- **Visual appeal** - Professional layouts with images and styling
- **Current information** - Real-time news and featured content
- **Easy setup** - Copy-paste card configurations

#### Technical Advantages
- **Single data source** - Simplified maintenance and updates
- **Improved reliability** - Better error handling and fallbacks
- **Performance optimized** - Efficient JSON parsing and processing
- **Future-proof** - Uses standard church website JSON API

### 🎯 Use Cases

#### News Dashboard
- Display latest church news headlines
- Show featured church content
- Create news-focused layouts
- Mobile-friendly news consumption

#### Complete Church Dashboard
- All-in-one spiritual content display
- Scripture, quotes, news, and featured content
- Comprehensive daily church content
- Rich media integration

#### Specialized Layouts
- News-only cards for current events
- Featured content for church resources
- Grid layouts for visual appeal
- Compact layouts for space efficiency

## [3.0.1] - 2025-10-23

### 🐛 Critical Bug Fixes

#### Fixed Coordinator Import Issues
- **Resolved circular import** between `__init__.py` and `sensor.py`
- Moved `LDSDataUpdateCoordinator` to proper location in `__init__.py`
- Removed duplicate coordinator class from `sensor.py`
- Fixed type hints using `TYPE_CHECKING` to avoid runtime import issues
- **This resolves the issue where sensors weren't being created properly**

### 🔧 Code Quality Improvements
- Added `.gitignore` to exclude Python cache files
- Improved import structure and removed circular dependencies
- Better separation of concerns between modules

## [3.0.0] - 2025-10-23

### 🎉 MAJOR RELEASE - Complete Rewrite

#### ⚠️ BREAKING CHANGES
- **Custom JavaScript cards removed** - Now uses standard markdown cards
- **Single sensor replaced** with multiple focused sensors
- **Installation process simplified** - No custom card management needed
- **Data structure changed** - See migration guide for details

#### 🆕 New Features
- **Multiple focused sensors**:
  - `sensor.lds_daily_scripture_eng` - Daily scripture with text and reference
  - `sensor.lds_daily_quote_eng` - Inspirational quotes from church leaders
  - `sensor.lds_come_follow_me_eng` - Current Come Follow Me lesson info
  - `sensor.lds_inspirational_image_eng` - Inspirational images with quotes
- **Standard markdown cards** with beautiful styling examples
- **Improved data fetching** with fallback content for reliability
- **Better error handling** and logging throughout
- **Simplified architecture** using standard HA patterns

#### 🗑️ Removed
- Custom JavaScript card files (`www/` directory)
- Complex web scraping of internal church website data
- Frontend resource registration system
- Multiple obsolete documentation files
- Custom installation scripts

#### 📚 New Documentation
- `MARKDOWN_CARDS_EXAMPLES.md` - Comprehensive card examples with styling
- `MIGRATION_GUIDE.md` - Step-by-step upgrade guide from v2.x
- `CLEANUP_SUMMARY.md` - Documentation of cleanup process

#### ✨ Benefits
- **More reliable**: No custom JavaScript dependencies
- **Better performance**: Native HA rendering
- **Universal compatibility**: Works on all devices and apps
- **Future-proof**: Uses standard HA patterns
- **Easier maintenance**: Simpler, cleaner codebase

## [2.0.2] - 2025-09-18

### 🐛 Critical Bug Fixes

#### Fixed Sensor AttributeError
- **Resolved sensor loading crash** caused by incorrect attribute name
- Fixed `AttributeError: 'LDSDataUpdateCoordinator' object has no attribute 'last_update_success_time'`
- Changed to correct attribute name `last_update_success`
- Sensor now loads properly without errors

#### Fixed Template Processing Errors
- **Resolved template crashes** with robust null-safe syntax
- Fixed `UndefinedError: 'None' has no attribute 'loaderData'` in automation examples
- Updated all template examples with proper null checking
- Templates now gracefully handle sensor loading states and missing data

### 📚 Enhanced Documentation

#### Comprehensive Setup Instructions
- **Added prominent warnings** about required resource registration for custom cards
- Enhanced CARDS_SETUP.md with step-by-step UI instructions
- Created comprehensive TROUBLESHOOTING.md guide covering common issues
- Updated README.md with immediate setup warnings and clear instructions

#### Custom Cards Documentation
- Clear explanation of "Custom element doesn't exist" errors and solutions
- Step-by-step resource registration process
- Verification steps and restart requirements
- Browser cache clearing instructions

#### Template Documentation
- Safe template examples with null checking
- Migration guide from problematic templates
- Best practices for robust automation templates
- Diagnostic commands for troubleshooting

### 🔧 User Experience Improvements
- **Clearer error messages** and troubleshooting steps
- **Better setup flow** preventing common configuration mistakes
- **Comprehensive troubleshooting** covering installation, cards, and templates
- **Faster issue resolution** with detailed diagnostic guides

## [2.0.1] - 2025-09-18

### 🐛 Bug Fixes

#### Fixed Dependency Conflicts
- **Resolved installation issues** caused by strict version pinning in dependencies
- Changed from `requests==2.31.0` to `requests>=2.28.0` to prevent conflicts with Home Assistant's package versions
- Updated `beautifulsoup4==4.12.3` to `beautifulsoup4>=4.12.0` for better compatibility
- Updated `chardet==3.0.4` to `chardet>=3.0.4` to maintain minimum requirements
- This fixes the error: "Unable to install package requests==2.31.0: No solution found when resolving dependencies"

#### Technical Improvements
- More flexible dependency management following Home Assistant best practices
- Future-proof package requirements that work with newer Home Assistant versions
- Better compatibility with HACS installation process

## [2.0.0] - 2025-09-18

### 🎉 Major Release - Complete Overhaul

This is a massive upgrade that transforms the LDS integration from a basic sensor to a comprehensive spiritual content platform for Home Assistant.

### ✨ New Features

#### 🎨 Custom Lovelace Cards
- **LDS Quote Card** - Beautiful gradient card displaying daily inspirational quotes
- **LDS Scripture Card** - Elegant card for daily scripture verses
- **LDS Come Follow Me Card** - Weekly study material card with study links
- **LDS Inspirational Picture Card** - Random inspirational picture quotes with images

#### 🖼️ Inspirational Picture Quotes
- Added integration with Church's Inspirational Picture Quotes collection
- Random selection from hundreds of scripture-based inspirational images
- Refresh functionality to get new quotes on demand
- High-resolution image support
- Direct links to original sources

#### 🔧 Services & Automation
- **lds.refresh_data** service for manual data updates
- Enhanced entity refresh capabilities
- Better automation integration support
- Service calls for card refresh buttons

#### 📚 Enhanced Documentation
- Comprehensive setup guides (CARDS_SETUP.md)
- Example dashboard configurations (EXAMPLES.md)
- Mobile-optimized layouts
- Multi-language support examples
- Troubleshooting guides

#### 🏠 HACS Integration
- Full HACS compatibility with hacs.json
- "Open in Home Assistant" quick install buttons
- Proper repository structure for automatic updates
- Version management and releases

### 🔄 Improvements

#### 🎯 Better Data Structure
- Enhanced error handling and validation
- Improved sensor state management
- Better attribute organization
- More robust data fetching

#### 📱 Mobile Optimization
- Responsive card designs
- Mobile-first dashboard examples
- Touch-friendly interfaces
- Optimized image loading

#### 🌍 Multi-Language Ready
- Enhanced language support framework
- Better language configuration
- Multi-language dashboard examples

#### ⚡ Performance Enhancements
- Optimized data fetching
- Better caching mechanisms
- Reduced API calls
- Faster card rendering

### 🛠️ Technical Changes

#### 📦 Dependencies
- Added beautifulsoup4 for better HTML parsing
- Updated requirements specifications
- Better dependency management

#### 🏗️ Code Structure
- Separated services into dedicated module
- Enhanced error handling throughout
- Better logging and debugging
- Improved code organization

#### 🔒 Security & Reliability
- Better error handling for network issues
- Graceful degradation when services are unavailable
- Input validation and sanitization
- Timeout handling

### 📋 Installation & Setup

#### Easy Installation
- HACS integration for one-click install
- Automated card installation script
- Clear setup instructions
- "Open in Home Assistant" buttons

#### Resource Management
- Organized card files in www/ directory
- Proper resource loading
- Clear file structure
- Installation verification

### 🎨 User Experience

#### Beautiful Design
- Modern gradient card designs
- Consistent color schemes
- Professional typography
- Responsive layouts

#### Intuitive Interface
- Clear navigation and controls
- Helpful tooltips and labels
- Easy configuration options
- User-friendly error messages

#### Rich Content
- High-quality images
- Formatted text display
- Interactive elements
- Direct links to sources

### 🔧 Configuration Examples

Added extensive configuration examples:
- Complete dashboard layouts
- Mobile-optimized configurations
- Multi-language setups
- Automation examples
- Template sensor examples

### 📖 Documentation

#### Comprehensive Guides
- Step-by-step setup instructions
- Troubleshooting guides
- Advanced configuration examples
- Performance optimization tips

#### Example Dashboards
- Family dashboard integration
- Morning routine dashboard
- Study focus dashboard
- Minimalist layouts
- Multi-language support

### 🐛 Bug Fixes

- Fixed sensor state evaluation logic
- Improved error handling for network issues
- Better handling of missing data
- Fixed attribute access patterns
- Resolved timeout issues

### ⚠️ Breaking Changes

- **Sensor State Logic**: Changed from checking `dateRange` to proper data validation
- **File Structure**: Cards moved to dedicated www/ directory
- **Configuration**: Enhanced configuration options may require setup review

### 🔄 Migration Guide

If upgrading from v1.x:
1. Update the integration through HACS or manually
2. Install the new custom cards using the provided script
3. Update your dashboard configurations
4. Review and update any automations using the sensor

### 🎯 Coming Next

Future enhancements planned:
- Additional card designs and themes
- More interactive features
- Enhanced automation triggers
- Additional content sources
- User personalization options

---

## [1.0.0] - Previous Release

### Features
- Basic daily scripture sensor
- Daily quote integration
- Come, Follow Me data
- Multi-language support
- Basic markdown card examples

---

## 🙏 Acknowledgments

- Thanks to the Home Assistant community for inspiration
- Data sourced from churchofjesuschrist.org
- Built with love for spiritual growth in smart homes
