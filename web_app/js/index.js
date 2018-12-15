
$(function()
{
    // sync the file input and text input
    $("#local_image").change(function () {        
        $("#local_image_path").val($(this).val());
    });

    // bind click to submit online image detect
    $("#online_image_submit").click(function()
    {
        $.post("/detect/online", {"online_image_url": $("#online_image_url").val()}, function(data, status, xhr){
            $("#json_result").text(JSON.stringify(data, null, 4))
            $("#image_result").attr("src", data["image"])
        }, "json");
    });

    // bind click to submit local image detect
    $("#local_image_submit").click(function()
    {
        $("#local_image_form").ajaxSubmit({
            success: function(data) {
                $("#json_result").text(JSON.stringify(data, null, 4))
                $("#image_result").attr("src", data["image"])
            },
            url: "/detect/local",
            type: "post",
            dataType: "json"
        });

    });
})
