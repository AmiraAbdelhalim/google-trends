function submit_data() {
        $.ajax({
            url: "",
            type: 'POST',  // http method
            data: {
                kw_list: document.getElementById('keyword').value,
                start_date: document.getElementById('start_date').value,
                start_time: document.getElementById('start_time').value,
                end_date: document.getElementById('end_date').value,
                end_time: document.getElementById('end_time').value
             },  // data to submit
            success: function (data) {
                console.log(data, '88888')
                if(!data.error) {
                   get_interests();
                }
            },
            error: function (jqXhr, textStatus, errorMessage) {
                    alert(errorMessage);
            }
        });
    }

    function get_interests() {
        var keyword = document.getElementById('keyword').value;
        $.ajax({
        type: "GET",
        url: `/trends/${keyword}`,
        data: {},
        success: function(data) {
            console.log('data ', data)
            if(!data.success) {
                document.getElementById('keyword').value = "";
                alert(data.msg);
            }
            else {
                document.getElementById('keyword').value = data.search_keyword;
                draw_chart(data)
            }
        }
       });
    }


   function draw_chart(data) {
    am4core.useTheme(am4themes_animated);
   // get interests data


    // Create chart instance
    var chart = am4core.create("chartdiv", am4charts.XYChart);

    // Add data
    chart.data = data.interests;

    // Create axes
    var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
    dateAxis.dataFields.category = "Date";
    dateAxis.renderer.grid.template.location = 0.5;
    dateAxis.dateFormatter.inputDateFormat = "M/d/yyyy";
    dateAxis.renderer.minGridDistance = 70;




    var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

    // Create series
    var series = chart.series.push(new am4charts.LineSeries());
    series.dataFields.valueY = "trends";
    series.dataFields.dateX = "date_time";
    series.strokeWidth = 0.5
    series.strokeOpacity = 0.3;

    var bullet = series.bullets.push(new am4charts.CircleBullet());
    bullet.strokeWidth = 0.5;
    bullet.stroke = am4core.color("#fff")

    chart.legend = new am4charts.Legend();
    chart.cursor = new am4charts.XYCursor();
   }

    // validate user added keywords
    $(".validate").on("click", function () {
        if (!valid()) {
            alert("Please, provide a keyword.");
            return false;
        }
    });

    function valid() {
        let keyword = document.getElementById('keyword').value;
        console.log('keyword ', keyword);
        return keyword ? true : false;
    }