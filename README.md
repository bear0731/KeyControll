檔案說明:  
key_binding：自訂義動作對應的鍵盤訊號。  
websocket_client：模擬收到動作後，產生對應的鍵盤訊號。  
websocjet_server：模擬 kinect 丟字串到 client。  
  
使用說明:  
先啟動client.py，再啟動server.py。  
btw，可以在client、server端啟動的同時，更改自訂義鍵盤訊號，不會炸裂。  

# Update: 更新功能，可接收Kinect組傳來的資料並執行
