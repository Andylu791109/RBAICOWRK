# 同仁 AI 工作助手｜啟動 Prompt

課程負責人依同仁部門，把對應那一段整段交給他。同仁複製整段貼進自己在用的 AI 就會開始，不需要下載或上傳任何檔案。

一次問一題，選代號就能回答。手邊沒有材料也可以開始。

---

## 業務部

```text
請完整讀取以下文件，依其中規則開始協助我工作：
https://raw.githubusercontent.com/Andylu791109/RBAICOWRK/main/departments/agents/SALES.md

不要摘要文件，讀取成功後直接開始第 1 題。一次只問一題，讓我能只答代號。若無法讀取，請明說並停止，不要假裝已讀。
```

## 財務部

```text
請完整讀取以下文件，依其中規則開始協助我工作：
https://raw.githubusercontent.com/Andylu791109/RBAICOWRK/main/departments/agents/FINANCE.md

不要摘要文件，讀取成功後直接開始第 1 題。一次只問一題，讓我能只答代號。若無法讀取，請明說並停止，不要假裝已讀。
```

## 行銷部

```text
請完整讀取以下文件，依其中規則開始協助我工作：
https://raw.githubusercontent.com/Andylu791109/RBAICOWRK/main/departments/agents/MARKETING.md

不要摘要文件，讀取成功後直接開始第 1 題。一次只問一題，讓我能只答代號。若無法讀取，請明說並停止，不要假裝已讀。
```

## 產品部

```text
請完整讀取以下文件，依其中規則開始協助我工作：
https://raw.githubusercontent.com/Andylu791109/RBAICOWRK/main/departments/agents/PRODUCT.md

不要摘要文件，讀取成功後直接開始第 1 題。一次只問一題，讓我能只答代號。若無法讀取，請明說並停止，不要假裝已讀。
```

## SPA

```text
請完整讀取以下文件，依其中規則開始協助我工作：
https://raw.githubusercontent.com/Andylu791109/RBAICOWRK/main/departments/agents/SPA.md

不要摘要文件，讀取成功後直接開始第 1 題。一次只問一題，讓我能只答代號。若無法讀取，請明說並停止，不要假裝已讀。
```

## 跨部門平台業績

```text
請完整讀取以下文件，依其中規則開始協助我工作：
https://raw.githubusercontent.com/Andylu791109/RBAICOWRK/main/departments/agents/CROSS_DEPARTMENT.md

不要摘要文件，讀取成功後直接開始第 1 題。一次只問一題，讓我能只答代號。若無法讀取，請明說並停止，不要假裝已讀。
```

## 人資與總務行政

```text
請完整讀取以下文件，依其中規則開始協助我工作：
https://raw.githubusercontent.com/Andylu791109/RBAICOWRK/main/departments/agents/HR_ADMIN.md

不要摘要文件，讀取成功後直接開始第 1 題。一次只問一題，讓我能只答代號。若無法讀取，請明說並停止，不要假裝已讀。
```

## 尚未校準的部門（直播、客服、出貨倉庫、採購）

這幾個部門還沒有主管校準資料，先用通用流程：

```text
請完整讀取以下文件，依照其中的「AI 執行規則」開始帶我設定：
https://raw.githubusercontent.com/Andylu791109/RBAICOWRK/main/AI_WORK_PARTNER_WIZARD.md

請一次只問一題，不要先摘要整份文件，也不要一次列出全部問題。如果我不知道怎麼回答，請依照我的部門提供具體選項或案例。若無法讀取，請明說並停止，不要假裝已讀。
```

---

## 給課程負責人的操作說明

1. 依同仁部門，複製對應那一整段（含連結）交給他。
2. 提醒他要**整段貼進 AI 送出**，不是只點開網址。
3. 同仁手邊沒有材料也能開始，AI 會用清楚標示的虛構示例帶他練。
4. 如果 AI 說讀不到網址，或只回了一段摘要，請同仁把畫面截圖回報，改用複製全文的方式。
5. 部門指令內的工作選項只是預設。同仁今天做的不是那幾項時，選「E｜今天不是這幾項」，AI 會改照他實際的工作協助。
6. 完成工作後，請同仁在**同一段對話**使用下方「留下本次學習紀錄」指令；AI 只產生草稿，不會自行提交 GitHub。

## 留下本次學習紀錄

同仁完成一項工作後，把這段貼回同一段 AI 對話：

```text
請依本次對話，整理一筆「AI 協作學習紀錄」。先讀取下列公開範本，完整保留第 1 部分固定欄位與第 2 部分自述：
https://raw.githubusercontent.com/Andylu791109/RBAICOWRK/main/templates/AI_LEARNING_REPORT_TEMPLATE.md

只記錄本次實際發生、可以從對話觀察到的事。record_id、learner_id、日期、主管確認或舊紀錄若未提供，填「未提供」或「未驗收」，不要猜。沒有修正就照實寫，不要硬湊進步。若範本網址讀不到，請明說並請我貼上範本全文，不要自行補欄位。

請先提醒我遮蔽客戶、同仁、訂單、未公開數字等資訊，再給可保存的草稿。這份草稿不會自動傳到 GitHub；主管檢查且確認可公開後，才由有權限的人提交。
```

能否讀取連結並直接執行，仍取決於各 AI 平台的能力與規則，不保證跨平台一致。
