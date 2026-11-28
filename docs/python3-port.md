# Python 3 port — fd-replay

Decision recorded on 2026-11-28: retain this project and prepare a Python 3 port.
This is a porting plan, not a compatibility claim or a published release.

## Current baseline

The current source remains Python 2-only (`python_requires='<3'`). No runtime
conversion or dependency upgrade is included in this preparation. Existing
published versions are unchanged. The repository currently has no executable
test suite to establish behavioural parity; creating that baseline is the first
implementation milestone.

## Observed migration work

- `fd_replay/classes/plugins.py` imports `Queue`; configuration and replay modules use `iteritems()` and Python 2 exception syntax.
- `fd_replay/plugins/http.py` uses `basestring`; define text/bytes boundaries for headers, bodies and libcurl callbacks.
- Characterize multi-target replay, body fidelity, header filtering, timeouts, error isolation and worker shutdown with local synthetic HTTP targets.
- Preserve endpoint configuration and credential loading contracts; never replay production traffic into new targets during tests.

## Implementation and acceptance sequence

1. Record current CLI/configuration contracts and build deterministic fixtures.
   Add a discovered test suite; report collected, executed and skipped counts.
2. Review current DWho, HTTPdis and Sonicprobe APIs, then select compatible
   versions and a supported Python 3 matrix. Reuse shared behaviour in those
   libraries instead of duplicating it here.
3. Port imports, exception syntax, mapping iteration and bytes/text handling.
   Upgrade third-party adapters separately, with migration notes for changed
   authentication or configuration.
4. Run unit and isolated integration tests on every claimed interpreter. Check
   clean installation, package metadata, CLI startup and graceful shutdown from
   the built wheel outside the source checkout.
5. Build reproducible candidate artifacts with explicit runtime file allow-lists.
   Exclude this plan, tests and maintainer files. Qualify the actual artifacts,
   then update `python_requires`, README instructions and release notes together.
6. Publish a new version only after qualification. Do not overwrite old packages
   or advertise the Python 3 port as complete before its acceptance checks pass.

## Delivery state

- [x] Preserve the repository and record the migration decision.
- [x] Make the current Python 2 restriction explicit to installers and readers.
- [ ] Behavioural baseline and test discovery established.
- [ ] Shared-library and external-adapter compatibility qualified.
- [ ] Python 3 runtime port and integration tests complete.
- [ ] Candidate artifact qualified and new release published.
