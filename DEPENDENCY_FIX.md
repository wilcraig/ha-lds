# Dependency Conflict Fix

## Issue
The integration was experiencing dependency conflicts with the `requests` package:
```
Unable to install package requests==2.31.0: × No solution found when resolving dependencies:
╰─▶ Because you require requests==2.31.0 and requests==2.32.4, we can conclude that your requirements are unsatisfiable.
```

## Root Cause
The manifest.json was using strict version pinning (`==`) for dependencies, which created conflicts when Home Assistant had newer versions of the same packages installed.

## Solution
Changed the requirements specification from strict version pinning to minimum version requirements:

**Before:**
```json
"requirements": ["chardet==3.0.4", "beautifulsoup4==4.12.3", "requests==2.31.0"]
```

**After:**
```json
"requirements": ["chardet>=3.0.4", "beautifulsoup4>=4.12.0", "requests>=2.28.0"]
```

## Benefits
- ✅ Allows Home Assistant to use compatible newer versions
- ✅ Prevents dependency conflicts
- ✅ Maintains minimum version requirements for functionality
- ✅ More flexible and future-proof

## Testing
After this change, the integration should install without dependency conflicts while maintaining all functionality.

## Version Compatibility
- `requests>=2.28.0`: Supports all modern HTTP features needed
- `beautifulsoup4>=4.12.0`: HTML parsing compatibility
- `chardet>=3.0.4`: Character encoding detection

This fix ensures the integration works with current and future Home Assistant versions.
