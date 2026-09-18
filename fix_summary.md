## Summary of Changes

### Problem
False positive 'Failed to load downloadfile.bin' media errors were occurring when AnkiDroid JS API calls failed or were unavailable. These JS exceptions were being misinterpreted by the WebView's error handler as missing media resources.

### Solution
Implemented a safe API call wrapper that:
1. Checks if the API and method exist before calling
2. Wraps API calls in Promise.resolve/null for consistency
3. Catches and logs any exceptions instead of letting them propagate
4. Returns null on failure to indicate API unavailability

### Files Modified
- Card 1 - Front.template.anki: Added safeApiCall wrapper and replaced direct API calls

### Specific Changes
1. Added detection for AnkiDroidJS in bridgeAvailable function
2. Created safeApiCall wrapper function with proper error handling
3. Replaced api.init(JSON.stringify(options)) with safeApiCall("init", JSON.stringify(options))
4. Replaced api.ankiGetCardInterval() with safeApiCall("ankiGetCardInterval")

### Verification
- All compactor regression tests pass (31/31)
- All template structural invariants pass (39/39)
- No regressions introduced

The fix prevents JS exceptions from API calls from triggering the WebView's media error handler, eliminating false positive media errors while maintaining correct functionality when the API is available.
