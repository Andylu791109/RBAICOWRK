# CLAUDE.md — 森呼吸 AI 工作夥伴（RBAICOWRK）

> ⚠️ **這是公開 repo。** 同仁的 AI 要靠 `raw.githubusercontent.com` 讀取本專案檔案，
> 所以必須公開。**任何內部經營數據、人事資訊、未定案決策、主管個人評論都不要寫進來。**

## 這個 repo 是什麼

森呼吸集團「AI 工作力實戰」課程的**主體**——同仁與講師實際會用到的東西都在這裡。

| 目錄 | 內容 | 誰用 |
| :-- | :-- | :-- |
| 根目錄 | `START_HERE.md`、`WORKER_START_PROMPT.md`、`AI_WORK_PARTNER_WIZARD.md`、`COMPANY_AI_RULES.md` | 同仁 |
| `departments/` | 九個部門的情境校準與 agent 設定 | 同仁（依部門） |
| `platform-guides/` | ChatGPT／Claude／Codex／Gemini 操作指南 | 同仁 |
| `templates/` | 個人設定範本、學習紀錄範本 | 同仁 |
| `course/` | 學員練習包、需求釐清引導 | 學員 |
| `facilitator/` | 開課手冊、主管校準精靈、講師講稿、交付檢查 | 講師／主管 |
| `docs/` | 簡報網頁版（互動簡報、執行長審閱版） | 課堂／課後複習 |

## 建構基礎資料在哪（不在這個 repo）

課程的**設計脈絡、決策過程、問卷統計、執行長回饋、簡報母檔**存放在 Andy 的
私有 repo `Andylu791109/andy-ai-agent`，路徑 `100_Todo/projects/客服部/AI內訓課程/`。

那裡有：25 份討論交接文件（`00_`～`24_`）、簡報 PDF／PPTX 母檔、原始圖素材、
建置腳本、歷史備份。**要理解「為什麼這樣設計」時去讀那裡；要改同仁看得到的東西改這裡。**

這些資料留在私有 repo 是刻意的——它們含內部經營資訊，不適合公開。

## 改東西的規則

- 改 `departments/` 或 `WORKER_START_PROMPT.md` 前，先確認該部門是否已完成主管訪談校準；
  未校準的部門（直播、客服、出貨倉庫、採購）走通用流程，不要自行編造情境。
- 同仁靠 raw 網址讀取，**檔名與路徑一旦公布就不要隨意更動**，會讓已發出去的連結失效。
- 改動後同步更新 `CHANGELOG.md`。
- 簡報網頁改動請一併更新私有 repo 的母檔，避免兩邊分岔。
