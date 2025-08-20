

function startDraw() {
    const button = document.getElementById('drawBtn');
    const result = document.getElementById('result');
    
  
    button.disabled = true;
    button.textContent = '抽獎中...';
    
    result.style.display = 'none';


    setTimeout(() => {
        
      
        fetch('/draw', {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            
            document.getElementById('resultCat').textContent = data.name;
            document.getElementById('resultMeaning').textContent = data.meaning;
            result.style.display = 'block';
            
          
            button.disabled = false;
            button.textContent = '再次抽獎';
        })
        .catch(error => {
            console.error('抽獎失敗:', error);
            alert('抽獎失敗，請重試');
            
            button.disabled = false;
            button.textContent = '開始抽獎';
        });
    }, 2000);
}