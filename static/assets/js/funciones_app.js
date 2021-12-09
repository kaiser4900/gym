
function getData(){
    $.ajax({
      type: "GET",
      url: '/test_ag/', 
      dataType: "json",
      success: function(data){
        $.each(data,function(key, registro) {
          $("#Select").append('<option value='+registro.id+'>'+registro.nivel+'</option>');
        });
        //setInterval('location.reload()', 1000000);  
        //$('#Select').selectpicker('refresh');        
      },
      error: function(data) {
        alert('error');
      }
    });
  }


  function updateTraining(){
    $.ajax({
      type: "GET",
      url: '/home/update_training/', 
      dataType: "json",
      success: function(data){
        $.each(data,function(key, registro) {
          $("#updateTraining").append('<option value='+registro+'</option>');
        });
        //setInterval('location.reload()', 1000000);  
        //$('#Select').selectpicker('refresh');        
      },
      error: function(data) {
        alert('errors');
      }
    });
  }