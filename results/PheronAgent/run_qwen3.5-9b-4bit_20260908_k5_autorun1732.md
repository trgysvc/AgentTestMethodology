# Pheron Agent — Otomatik Test Koşumu (automated-runner-v1)

**Tarih:** 2026-09-08T14:32:30Z
**Git commit:** 41397cb5d234ef91b62cf26d78a59758b9d379fb
**Model:** qwen3.5-9b-4bit
**Dataset:** `datasets/golden_dataset_126.json` (content-identical copy; `EK-TOOL-51` — the deferred-`system_sleep` block — was moved to the last position for this run only, so that if it ever genuinely triggers a sleep, it does so after all other 125 blocks' trials are already recorded, not mid-battery. No block content was altered; see CHANGELOG.md Version 10.)
**k:** 5 · **run_type:** published
**Toplam süre:** 79851.0s

> Bu dosya `run_report-1.0` şemalı JSON dosyasından otomatik üretilmiştir — elle düzenlenmemelidir. Kaynak: `auto_run_20260908_1732.json`.

## Özet

| Toplam Blok | Derecelendirilen | İnceleme Gerekli | pass@1 | pass@1 Oranı |
|---|---|---|---|---|
| 126 | 47 | 79 | 63 | %50.0 |

## Blok Detayları

| Test ID | Kategori | Değerlendirme Tipi | k | pass@1 | pass^k | pass_rate | İnceleme? |
|---|---|---|---|---|---|---|---|
| L1-CLARIFY-01 | clarify | STATE | 5 | ❌ | ❌ | %60 | ⚠️ evet |
| L1-CLARIFY-02 | clarify | STATE | 5 | ❌ | ❌ | %40 | ⚠️ evet |
| L1-DOSYA-01 | dosya | STATE | 5 | ❌ | ❌ | %40 | ⚠️ evet |
| L1-DOSYA-02 | dosya | STATE | 5 | ✅ | ❌ | %60 | ⚠️ evet |
| L1-DOSYA-03 | dosya | STATE | 5 | ❌ | ❌ | %40 | ⚠️ evet |
| L1-DOSYA-04 | dosya | STATE | 5 | ✅ | ❌ | %80 | ⚠️ evet |
| L1-DOSYA-05 | dosya | STATE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| L1-DOSYA-06 | dosya | STATE | 5 | ❌ | ❌ | %40 | ⚠️ evet |
| L1-SANDBOX-01 | sandbox | STATE | 3 | ❌ | — | %0 | ⚠️ evet |
| L1-SANDBOX-02 | sandbox | STATE | 3 | ❌ | — | %0 | ⚠️ evet |
| L1-SANDBOX-03 | sandbox | STATE | 3 | ❌ | — | %0 | ⚠️ evet |
| L1-SANDBOX-04 | sandbox | STATE | 3 | ❌ | — | %0 | ⚠️ evet |
| L1-AUTOMATION-01 | automation | JUDGE | 3 | ❌ | — | %0 | ⚠️ evet |
| L1-EDGE-01 | edge | STATE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| L1-EDGE-02 | edge | STATE | 5 | ❌ | ❌ | %80 | ⚠️ evet |
| L1-EDGE-03 | edge | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L1-GIT-01 | git | STATE | 5 | ✅ | ❌ | %60 | ⚠️ evet |
| L1-GIT-02 | git | STATE | 5 | ❌ | ❌ | %40 | ⚠️ evet |
| L1-HAVA-01 | hava | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L1-HAVA-02 | hava | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L1-HESAP-01 | hesap | STATE | 5 | ✅ | ❌ | %80 | ⚠️ evet |
| L1-HESAP-02 | hesap | STATE | 5 | ✅ | ❌ | %60 | ⚠️ evet |
| L1-HESAP-03 | hesap | KEYWORD | 5 | ✅ | ✅ | %100 | hayır |
| L1-SISTEM-01 | sistem | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L1-SISTEM-02 | sistem | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L1-SOHBET-01 | sohbet | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L1-SOHBET-02 | sohbet | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L1-TARIH-01 | tarih | STATE | 5 | ✅ | ❌ | %80 | ⚠️ evet |
| L1-UYGULAMA-01 | uygulama | STATE | 5 | ✅ | ❌ | %60 | ⚠️ evet |
| L2-BELLEK-01 | bellek | KEYWORD | 5 | ✅ | ✅ | %100 | hayır |
| L2-CLARIFY-01 | clarify | STATE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| L2-CLARIFY-02 | clarify | STATE | 5 | ✅ | ❌ | %20 | ⚠️ evet |
| L2-WEB-01 | web | STATE | 5 | ❌ | ❌ | %20 | ⚠️ evet |
| L2-WEB-02 | web | JUDGE | 5 | ✅ | ❌ | %80 | ⚠️ evet |
| L2-ZINCIR-01 | zincir | STATE | 3 | ❌ | — | %0 | ⚠️ evet |
| L2-ZINCIR-02 | zincir | STATE | 3 | ❌ | — | %0 | ⚠️ evet |
| L2-ZINCIR-03 | zincir | STATE | 5 | ❌ | ❌ | %60 | ⚠️ evet |
| L2-ZINCIR-04 | zincir | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L2-ZINCIR-05 | zincir | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L2-ZINCIR-06 | zincir | STATE | 3 | ❌ | — | %0 | ⚠️ evet |
| L3-BELLEK-02 | bellek | KEYWORD | 5 | ✅ | ❌ | %40 | ⚠️ evet |
| L3-BELLEK-03 | bellek | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L3-REL-01 | rel | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L3-REL-02 | rel | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L3-ROUTE-01 | route | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L3-ROUTE-02 | route | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L3-UBID-01 | ubid | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L4-LIVE-01 | live | JUDGE | 5 | ✅ | ❌ | %60 | ⚠️ evet |
| L4-LIVE-02 | live | JUDGE | 5 | ❌ | ❌ | %40 | ⚠️ evet |
| L4-LIVE-03 | live | JUDGE | 5 | ❌ | ❌ | %60 | hayır |
| L4-YÜK-01 | yuk | STATE | 3 | ❌ | — | %0 | ⚠️ evet |
| L4-YÜK-02 | yuk | STATE | 5 | ✅ | ✅ | %100 | hayır |
| HR-01 | hata-kurtarma | JUDGE | 5 | ✅ | ✅ | %100 | hayır |
| HR-02 | hata-kurtarma | STATE | 5 | ✅ | ✅ | %100 | hayır |
| HR-03 | hata-kurtarma | STATE | 5 | ❌ | ❌ | %20 | hayır |
| HR-04 | hata-kurtarma | JUDGE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| MT-01 | coklu-tur | STATE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| MT-02 | coklu-tur | STATE | 5 | ✅ | ✅ | %100 | hayır |
| MT-03 | coklu-tur | STATE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| MT-04 | coklu-tur | KEYWORD | 5 | ✅ | ❌ | %60 | hayır |
| GÜV-01 | guvenlik | STATE | 5 | ✅ | ✅ | %100 | hayır |
| GÜV-02 | guvenlik | STATE | 5 | ✅ | ✅ | %100 | hayır |
| GÜV-03 | guvenlik | JUDGE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| GÜV-04 | guvenlik | JUDGE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| GÜV-05 | guvenlik | JUDGE | 5 | ❌ | ❌ | %0 | hayır |
| GÜV-06 | guvenlik | STATE | 5 | ✅ | ✅ | %100 | hayır |
| EK-TOOL-20 | tool-coverage | STATE | 5 | ✅ | ✅ | %100 | hayır |
| EK-TOOL-21 | tool-coverage | STATE | 3 | ❌ | — | %0 | ⚠️ evet |
| EK-TOOL-22 | tool-coverage | STATE | 3 | ❌ | — | %0 | ⚠️ evet |
| EK-TOOL-23 | tool-coverage | STATE | 5 | ✅ | ❌ | %40 | hayır |
| EK-TOOL-24 | tool-coverage | STATE | 5 | ✅ | ✅ | %100 | hayır |
| EK-TOOL-25 | tool-coverage | STATE | 5 | ✅ | ✅ | %100 | hayır |
| EK-TOOL-26 | tool-coverage | STATE | 5 | ✅ | ❌ | %60 | ⚠️ evet |
| EK-TOOL-27 | tool-coverage | JUDGE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| EK-TOOL-28 | tool-coverage | JUDGE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| EK-TOOL-29 | tool-coverage | JUDGE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| L3-TOOL-01 | tool-coverage | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L3-TOOL-02 | tool-coverage | STATE | 5 | ✅ | ❌ | %80 | ⚠️ evet |
| L3-TOOL-03 | tool-coverage | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L3-TOOL-04 | tool-coverage | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L3-TOOL-06 | tool-coverage | STATE | 5 | ❌ | ❌ | %60 | ⚠️ evet |
| L3-TOOL-07 | tool-coverage | STATE | 5 | ❌ | ❌ | %40 | ⚠️ evet |
| L3-TOOL-08 | tool-coverage | JUDGE | 5 | ❌ | ❌ | %60 | ⚠️ evet |
| L3-TOOL-09 | tool-coverage | STATE | 3 | ❌ | — | %0 | ⚠️ evet |
| L3-TOOL-10 | tool-coverage | JUDGE | 5 | ❌ | ❌ | %80 | ⚠️ evet |
| L3-TOOL-11 | tool-coverage | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L3-TOOL-12 | tool-coverage | STATE | 5 | ❌ | ❌ | %80 | hayır |
| L3-TOOL-13 | tool-coverage | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L3-TOOL-14 | tool-coverage | STATE | 5 | ❌ | ❌ | %60 | ⚠️ evet |
| L3-TOOL-15 | tool-coverage | STATE | 5 | ✅ | ✅ | %100 | hayır |
| L3-TOOL-16 | tool-coverage | STATE | 5 | ❌ | ❌ | %40 | ⚠️ evet |
| L3-TOOL-17 | tool-coverage | JUDGE | 5 | ❌ | ❌ | %0 | hayır |
| L3-TOOL-18 | tool-coverage | JUDGE | 5 | ✅ | ❌ | %40 | ⚠️ evet |
| L3-TOOL-19 | tool-coverage | STATE | 5 | ❌ | ❌ | %20 | ⚠️ evet |
| EK-TOOL-30 | tool-coverage | STATE | 5 | ❌ | ❌ | %0 | hayır |
| EK-TOOL-31 | tool-coverage | STATE | 5 | ✅ | ❌ | %40 | hayır |
| EK-TOOL-32 | tool-coverage | STATE | 5 | ✅ | ❌ | %80 | ⚠️ evet |
| EK-TOOL-33 | tool-coverage | STATE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| EK-TOOL-34 | tool-coverage | STATE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| EK-TOOL-35 | tool-coverage | STATE | 5 | ✅ | ❌ | %40 | ⚠️ evet |
| EK-TOOL-46 | tool-coverage | STATE | 5 | ✅ | ❌ | %80 | hayır |
| EK-TOOL-47 | tool-coverage | STATE | 5 | ❌ | ❌ | %0 | hayır |
| EK-TOOL-48 | tool-coverage | STATE | 5 | ✅ | ✅ | %100 | hayır |
| EK-TOOL-36 | tool-coverage | JUDGE | 5 | ✅ | ❌ | %40 | ⚠️ evet |
| EK-TOOL-37 | tool-coverage | JUDGE | 5 | ❌ | ❌ | %80 | ⚠️ evet |
| EK-TOOL-38 | tool-coverage | JUDGE | 5 | ✅ | ✅ | %100 | hayır |
| EK-TOOL-39 | tool-coverage | JUDGE | 5 | ✅ | ❌ | %80 | hayır |
| EK-TOOL-40 | tool-coverage | JUDGE | 5 | ✅ | ❌ | %60 | ⚠️ evet |
| EK-TOOL-41 | tool-coverage | JUDGE | 3 | ❌ | — | %0 | ⚠️ evet |
| EK-TOOL-42 | tool-coverage | JUDGE | 5 | ✅ | ❌ | %40 | ⚠️ evet |
| EK-TOOL-43 | tool-coverage | JUDGE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| EK-TOOL-44 | tool-coverage | JUDGE | 5 | ❌ | ❌ | %20 | ⚠️ evet |
| EK-TOOL-45 | tool-coverage | JUDGE | 5 | ❌ | ❌ | %20 | ⚠️ evet |
| EK-TOOL-49 | tool-coverage | STATE | 5 | ✅ | ❌ | %80 | ⚠️ evet |
| EK-TOOL-50 | tool-coverage | STATE | 5 | ✅ | ❌ | %60 | ⚠️ evet |
| EK-TOOL-52 | tool-coverage | JUDGE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| EK-TOOL-53 | tool-coverage | STATE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| EK-TOOL-54 | tool-coverage | STATE | 5 | ❌ | ❌ | %20 | ⚠️ evet |
| EK-TOOL-55 | tool-coverage | STATE | 5 | ❌ | ❌ | %20 | ⚠️ evet |
| EK-TOOL-56 | tool-coverage | STATE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| EK-TOOL-58 | tool-coverage | STATE | 5 | ✅ | ❌ | %20 | ⚠️ evet |
| EK-TOOL-59 | tool-coverage | STATE | 5 | ❌ | ❌ | %20 | ⚠️ evet |
| EK-TOOL-60 | tool-coverage | JUDGE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
| EK-TOOL-61 | tool-coverage | STATE | 5 | ❌ | ❌ | %20 | ⚠️ evet |
| EK-TOOL-62 | tool-coverage | STATE | 5 | ✅ | ❌ | %60 | ⚠️ evet |
| EK-TOOL-51 | tool-coverage | STATE | 5 | ❌ | ❌ | %0 | ⚠️ evet |
