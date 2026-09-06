# Definition Truncation Feature - Handoff

## Initial Request
User wanted to add definition truncation feature with max lines and expand/collapse indicator.

## Iteration 1 - First Attempt
**Requirements:**
- Limit dictionary definition to a few lines
- Show indicator when truncated (arrow or similar)
- Indicator clickable to expand
- Never clog the whole screen

**Implementation:**
- CSS max-height of 3.1em (3 lines)
- Arrow indicator (▼) at bottom
- Gradient fade overlay
- JS toggle function

**User Feedback:** "horrible design"

**Changes Made:**
- Redesigned with pill-based "Expand" indicator
- Gradient overlay
- Kept max-height at 3.1em

**User Feedback:** "no need to type expand in front of the words... small arrow would have been enough"

## Iteration 2 - Arrow Only
**Requirements:**
- Just a small arrow indicator (no text)
- Progressive fade effect to show more content exists
- Show bottom part less visible as it gets to truncation point

**Implementation:**
- Subtle chevron (▼) indicator
- Progressive fade from transparent to background
- max-height: 3.1em

**User Feedback:** "nothing changed at all"

**Why Failed:**
- max-height alone doesn't work reliably in Anki's WebView environment
- CSS specificity issues
- max-height was being overridden by other styles

## Iteration 3 - Reduce to 2 Lines
**Requirements:**
- Reduce truncation to 1-2 lines
- Show bottom part less visible
- No up arrow indicator needed

**Implementation:**
- max-height: 2.2em (2 lines)
- Fade overlay adjusted to 1.3em height

**User Feedback:** "nothing changed at all"

**Why Failed:**
- Same fundamental issue - max-height approach doesn't work

## Iteration 4 - Reduce to 1.8em
**Requirements:**
- Even less truncation (1.8em ≈ 1 line)
- Adjust fade overlay

**User Feedback:** "nothing changed at all"

**Why Failed:**
- Same fundamental issue

## Iteration 5 - Final Attempt with line-clamp
**Requirements:**
- Fix the truncation properly
- Use reliable CSS approach for Anki

**Implementation:**
- Changed from max-height to CSS line-clamp
- Added `-webkit-line-clamp: 1`
- Used full selector `.definition-box.primary-definition` for specificity
- max-height: 1.5em (1 line)
- Fade overlay: 1.1em height

**Status:** Just synced to Anki
**Testing Needed:** User needs to verify if this finally works

## Technical Issues Identified

### Root Cause
The fundamental problem is that max-height alone doesn't work reliably in Anki's WebView. The styling conflicts with:
1. Yomitan's inline styles for definition glossary
2. Existing definition compactor CSS (section 6b)
3. Anki's CSS cascade

### Why max-height Failed
- Anki's WebView applies Yomitan's inline styles which have higher specificity
- The `.primary-definition` selector doesn't have enough specificity
- max-height is being overridden by other CSS rules
- The definition content structure from Yomitan (nested divs, spans) interferes with truncation

### CSS line-clamp Approach
The new approach uses:
```css
.definition-box.primary-definition {
  line-clamp: 1;
  -webkit-line-clamp: 1;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```

This is the modern, standard way to truncate text and should work better because:
1. It's explicitly designed for text truncation
2. Uses vendor prefixes for WebView compatibility
3. Has better specificity with full class names
4. Isn't fighting with layout properties

## What Needs Testing

1. **Open a card with a long definition**
2. **Verify 1 line is shown by default**
3. **Click to expand - does it show full definition?**
4. **Check if fade overlay appears**
5. **Verify chevron indicator shows**

## Files Modified
- `Card 1 - Style.css` - section 6c
- `Card 1 - Back.template.anki` - added tabindex, role, aria-expanded attributes

## To Finish
Run `./finish.sh --prompt "..." "Finalize truncation fix"` to push to main after user confirms it works.

## Alternative Approaches If This Fails

1. **Use JS-based truncation** on render time
2. **Change the HTML structure** (inject wrapper div before content)
3. **Use Anki field filter** to manually truncate in Yomitan
4. **Increase truncation threshold** significantly (4-5 lines) so effect is obvious
