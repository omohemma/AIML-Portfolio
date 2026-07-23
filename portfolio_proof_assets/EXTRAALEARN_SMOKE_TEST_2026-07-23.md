# ExtraaLearn App Smoke Test

Date: 2026-07-23

## Result

Passed on retry.

## What Passed

- Frontend Space loaded at `https://omohemma-extraalearn-frontend.hf.space/`.
- App title rendered: `ExtraaLearn Lead Conversion`.
- Single Lead form rendered with the expected fields.
- Backend URL field was populated with `https://omohemma-extraalearn-backend.hf.space`.
- Clicking `Predict Conversion` returned a prediction on retry.
- Default sample lead result: `Converted`.
- Default sample lead conversion probability: `76.0%`.

## Earlier Failure

- The first run failed because the backend Space was paused.
- The frontend showed a JSON decode error because the backend response was not valid JSON at that time.
- Direct backend health check returned: `The space is paused, ask a maintainer to restart it`.

## Evidence

- `screenshots/extraalearn-smoke-test-success.png`
- `screenshots/extraalearn-smoke-test-frontend-error.png`
- `screenshots/extraalearn-smoke-test-backend-paused.png`

## Next Action

No blocker remains for the default single-lead smoke path. Optional next test: batch CSV scoring.
