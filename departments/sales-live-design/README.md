# 森呼吸業務部直播設計 AI

這是 `RBAICOWRK` 全公司 AI 工具中的「業務部直播設計」專區。業務夥伴可用一般說話方式和 AI 一起做直播預告、IG 限時動態及 IG／FB 貼文。使用者不用會寫程式，也不用有 GitHub 帳號；只要開啟線上入口、提供需求與回饋即可。

其他部門或非直播設計需求，請回到 [公司共用入口](../../START_HERE.md) 選擇正確流程。

## 線上開始

1. 開啟 [`ONLINE_START.md`](ONLINE_START.md)。
2. 複製裡面的啟動指令，貼到 ChatGPT、Codex、Claude 或其他能讀取網頁的 AI。
3. AI 會一次問一題，帶你完成需求、Hero 主視覺、多尺寸延伸與檢查。
4. 完成後，把 AI 產出的《直播設計回報》交給主管或 repo 維護者。

如果使用的 AI 無法讀取網址，可開啟 [`SKILL.md`](SKILL.md)，複製全文貼入對話。

## 直接啟動文字

> 請讀取森呼吸業務部直播設計指引，依照指引一次問我一題，不要要求我會設計術語。這次我要製作直播宣傳圖。

如果你不知道尺寸、排版或怎麼描述風格，直接說「請依現有品牌資料先提出一版」。AI 只會追問真正會影響成品的資訊。

## 你每次需要提供什麼

盡量提供以下內容；缺少時 AI 會協助整理：

- 要宣傳的事情或商品。
- 發布平台，例如 IG Story、IG 貼文或 FB 貼文。
- 希望觀眾採取的行動，例如立即預約、觀看直播、私訊詢問。
- 必須出現的文字、日期、價格或活動條件。
- 可使用的商品照、人物照、Logo 或參考圖。
- 交付期限及是否需要多種尺寸。

## 怎麼給回饋

不用說設計術語。請描述你看到的問題和想達成的效果，例如：

- 「第一眼看不到直播日期。」
- 「標題太搶，商品反而不明顯。」
- 「CTA 被人物擋住了。」
- 「這個風格太像廉價促銷，希望更有留白。」
- 「這版可以，以後新品限動可沿用這種層級。」

越具體的回饋，越容易成為可重複使用的品牌記憶。

## AI 怎麼學會我們的習慣

學習分三層：

1. **單次修改**：例如「這次人物放右邊」，只記在 `DESIGN_LOG.md`。
2. **可能的品牌偏好**：例如多次覺得標題太大，先放進 `DESIGN_MEMORY.md` 觀察。
3. **固定規則**：使用者明確指定，或同一偏好在不同設計中重複驗證 2～3 次，才升級到 Skill 或設計規則。

因此，一次臨時修改不會立刻變成永久規定。AI 會保留情境與證據，避免越學越亂。

## 完成一張圖之後

請告訴 AI 哪個版本「採用」或「不採用」，並盡量說明原因。AI 會：

- 在 `knowledge/DESIGN_LOG.md` 記錄過程與最終版本。
- 把可能重複使用的偏好放進 `knowledge/DESIGN_MEMORY.md`。
- 將可公開且已去識別化的成品整理到 `examples/approved/`。
- 將有學習價值的退回版本整理到 `examples/rejected/`。

如果圖片含客戶資料、訂單、未公開價格或公司機密，不要上傳到公開 repo；只記錄去識別化的文字結論。

## 資料夾導覽

| 檔案／資料夾 | 用途 |
|---|---|
| `SKILL.md` | AI 的主要工作方法與學習規則 |
| `knowledge/BRAND_PROFILE.md` | 已確認的品牌資料 |
| `knowledge/COPY_STYLE.md` | 文案語氣與圖上文字習慣 |
| `knowledge/DESIGN_MEMORY.md` | 尚在累積證據的設計偏好 |
| `knowledge/DESIGN_LOG.md` | 每次製圖、修改與採用紀錄 |
| `references/SOCIAL_SIZES.md` | IG／FB 常用尺寸與多尺寸原則 |
| `references/DESIGN_RULES.md` | Mobile First、層級、CTA 與 QA 規則 |
| `references/WORKFLOW.md` | 從需求、Hero 到回饋學習的完整流程 |
| `examples/approved/` | 被採用的正例與原因 |
| `examples/rejected/` | 被退回的反例、問題與修正方式 |

## 主管如何查看

主管可直接查看：

- `knowledge/DESIGN_LOG.md`：每次直播設計、修改和最終採用結果。
- `knowledge/DESIGN_MEMORY.md`：正在累積證據的業務部直播設計偏好。
- `examples/approved/`：已採用案例及採用原因。
- `examples/rejected/`：未採用案例、問題與修正方向。

沒有 GitHub 帳號的業務夥伴無法直接把對話寫回 repo。因此每次流程最後會產生一份標準《直播設計回報》，由主管或 repo 維護者貼回 `DESIGN_LOG.md`。這能讓同仁維持簡單操作，同時讓主管看到完整紀錄。

詳見 [`SUPERVISOR_GUIDE.md`](SUPERVISOR_GUIDE.md)。
