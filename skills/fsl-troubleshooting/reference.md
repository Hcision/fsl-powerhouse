# Troubleshooting reference

Compiled on 2026-11-23. Each row names the documented cause to rule out first and the skill that holds the detail. Every cause comes from an official page cited in that skill's reference.

| Symptom | Check first | Skill |
| --- | --- | --- |
| No slots or no candidates | The policy has a database work rule that narrows candidates, ideally to about 20. The territory has a primary member. The running user holds a scheduling permission set | `fsl-scheduling` |
| Slots at the wrong time | The time zone passed to booking, the UTC conversion of the arrival window, and dates around a DST change | `fsl-scheduling` |
| Resource missing from the Gantt or never assigned | Resource active, Field Service Scheduling license, membership type and dates, shift inside a primary membership | `fsl-workforce-territories`, `fsl-security-licensing` |
| Optimization fails or skips appointments | All territories in the request use the same engine. Hourly and daily optimization limits. Pinned appointments are not counted | `fsl-scheduling`, `fsl-architecture` |
| Dependent appointments not scheduled together | All territories of the chain are in the request. Without Enhanced Scheduling and Optimization, Same Resource needs a single territory membership | `fsl-scheduling` |
| Maintenance work orders not generated | Generation status, one batch at a time, the 2,600 work orders per generation limit, and which record holds the date cursor | `fsl-preventive-maintenance` |
| Scheduling from a platform event fails | The trigger runs as Automated Process, which cannot schedule, unless a user is configured | `fsl-scheduling` |
| Custom Gantt list does not refresh | Enhanced Live Updates and read access to every field in the appointment field sets | `fsl-dispatch-console` |
| Dispatcher cannot edit a schedule | Sharing gives read-only instead of read and write on the territory's appointments | `fsl-security-licensing` |
| Technician cannot open the mobile app | Resource inactive, or mobile license and permission set missing | `fsl-security-licensing` |
| Offline priming error | Task objects in the briefcase | `fsl-mobile-offline` |
| LWC change not visible on iOS | The app needs a full quit and relaunch | `fsl-mobile-offline` |
| Stock quantity wrong | Which product item the consumption or transfer names, and whether the transfer was marked received | `fsl-inventory` |
| Service report not created by code | Signature types and count match the template. Guest user in a future method | `fsl-integration-data` |
