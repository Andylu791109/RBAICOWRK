# 森呼吸 AI 工作夥伴設定精靈

這是一套跨平台的 AI 協作設定工具。它不要求使用者先學會寫 Prompt，而是由 AI 用「一次一題、具體選項、依部門舉例」的方式，協助使用者辨認工作需求、補齊必要資訊、降低不精確回答，最後生成可攜式的個人 AI 工作夥伴設定。

## 立即開始

1. 開啟 [`START_HERE.md`](START_HERE.md)。
2. 把啟動指令與 [`AI_WORK_PARTNER_WIZARD.md`](AI_WORK_PARTNER_WIZARD.md) 的公開網址交給你正在使用的 AI。
3. 一次回答一題；不知道怎麼回答時，選擇「我不知道，請依我的工作情境舉例」。
4. 完成真實工作測試與至少一次修正。
5. 保存 AI 產出的個人設定與學習紀錄。

**給 AI 直接讀取的 Raw 網址：**
https://raw.githubusercontent.com/Andylu791109/RBAICOWRK/main/AI_WORK_PARTNER_WIZARD.md

## 完成後會得到什麼

- `我的AI工作夥伴設定.md`：可放進不同 AI 的個人或專案指令。
- 一項經過需求釐清、產出、檢查與修正的工作成果。
- `AI協作學習紀錄.md`：用於課程驗收與後續改善。

## 核心原則

- 不要求使用者憑空定義需求，先用選項協助辨認。
- 資訊不足時先釐清，不讓 AI 默默補完。
- 將內容區分為「已確認／合理推論／待確認」。
- 高風險事項必須由人確認。
- 個人設定必須經過真實工作測試後才能定稿。
- 出貨、倉庫、採購與直播等執行工作採用小白手把手問法，必要時每個選項附括號範例。

## Repo 導覽

| 內容 | 用途 |
|---|---|
| [`START_HERE.md`](START_HERE.md) | 給第一次使用的同仁 |
| [`AI_WORK_PARTNER_WIZARD.md`](AI_WORK_PARTNER_WIZARD.md) | AI 實際執行的互動引導文件 |
| [`COMPANY_AI_RULES.md`](COMPANY_AI_RULES.md) | 公司共通的 AI 協作底線 |
| [`PRIVACY_AND_SUBMISSION.md`](PRIVACY_AND_SUBMISSION.md) | 資料遮蔽與作業提交規則 |
| [`departments/`](departments/) | 各部門可辨認的工作情境 |
| [`departments/CALIBRATED_CONTEXT.md`](departments/CALIBRATED_CONTEXT.md) | 已收到的主管校準工作與驗收條件 |
| [`platform-guides/`](platform-guides/) | 各 AI 平台的保存方式 |
| [`templates/`](templates/) | 個人設定與學習紀錄格式 |
| [`facilitator/CLASS_GUIDE.md`](facilitator/CLASS_GUIDE.md) | 講師帶領與驗收流程 |
| [`facilitator/COMPATIBILITY_TEST.md`](facilitator/COMPATIBILITY_TEST.md) | 不同 AI 的相容性測試 |
| [`facilitator/SUPERVISOR_START_PROMPT.md`](facilitator/SUPERVISOR_START_PROMPT.md) | 可直接貼入任何 AI 的主管版啟動 Prompt |
| [`facilitator/SUPERVISOR_CALIBRATION_WIZARD.md`](facilitator/SUPERVISOR_CALIBRATION_WIZARD.md) | 由 AI 逐題訪談主管並回寫部門報告 |
| [`facilitator/SUPERVISOR_DEPARTMENT_CALIBRATION.md`](facilitator/SUPERVISOR_DEPARTMENT_CALIBRATION.md) | 主管部門情境校準表 |
| [`CHANGELOG.md`](CHANGELOG.md) | 版本與待完成事項 |

## 適用範圍

這套工具可交給能讀取網頁或 Markdown 內容的 AI 使用。如果 AI 無法讀取外部網址，請開啟文件後複製全文貼入對話。

本 Repo 不存放真實客戶資料、訂單資料、薪資、人事紀錄、財務數字、未公開產品資訊或公司機密。

目前已整合業務、財務、人資與總務行政、SPA，以及跨部門平台業績的去識別化主管回饋。原始訪談不放入公開 Repo。

## 主管校準入口

主管只需複製以下啟動 Prompt，貼入正在使用的 AI：

[主管部門校準｜一鍵啟動 Prompt](facilitator/SUPERVISOR_START_PROMPT.md)

啟動 Prompt 會要求 AI 讀取以下 Raw 文件，再依部門逐題訪談並產出《部門 AI 情境校準報告》：

https://raw.githubusercontent.com/Andylu791109/RBAICOWRK/main/facilitator/SUPERVISOR_CALIBRATION_WIZARD.md

## 設計說明

本專案借鑑「文件同時提供人類說明與 AI 執行指令」的互動式設定概念，全部問句、流程、部門案例與驗收機制均依本次企業 AI 內訓需求重新設計。參考來源見 [`NOTICE.md`](NOTICE.md)。
