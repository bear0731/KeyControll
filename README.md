# 檔案說明:  
- ### key_binding：
  - 自訂義動作對應的鍵盤訊號。  
  - 格式：`{"動作":"按鍵"}`
- ### Controller：模擬收到動作後，產生對應的鍵盤訊號。  
- ### websocjet_server：模擬 kinect 丟字串到 client。  
  
## 使用說明:  
- 先啟動Controller.py，再啟動server.py。  
- 要改按鍵（自定義）可透過Key_biding.py更改
- btw，可以在client、server端啟動的同時，更改自訂義鍵盤訊號，不會炸裂。  
- 更新功能（LastUpdate: 2024.05.28）：
    - 若`Controller`過久沒收到訊號（20秒），則會在螢幕上print出錯誤訊息。