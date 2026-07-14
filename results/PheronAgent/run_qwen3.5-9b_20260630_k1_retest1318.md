# Targeted Re-Test Results
Date: 2026-06-30 13:18
PASS: 5 | FAIL: 1

| ID | Status | Tools | Time |
|---|---|---|---|
| SISTEM-02 | ✅ | ['get_system_info', 'Querying system hardware/software info...'] | 0.0s |
| GIT-01 | ✅ | ['git_action', 'Executing Git version control operations...'] | 112.2s |
| UYGULAMA-01 | ✅ | ['learn_application_ui', 'Scanning application ecosystem...'] | 96.8s |
| UYGULAMA-02 | ✅ | ['app_launcher', 'Launching application...'] | 124.8s |
| ZINCIR-02 | ❌ Expected 'shell_exec' not in ['file_manager_action', 'Listing PheronAgent/...', 'read_file', 'Reading swift_demo.swift...'] | ['file_manager_action', 'Listing PheronAgent/...', 'read_file', 'Reading swift_demo.swift...'] | 123.9s |
| SAF-01 | ✅ | ['web_search', 'Searching: site:swift.org documentation...'] | 120.1s |
