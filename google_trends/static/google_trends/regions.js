
function submit_data() {
    $.ajax({
            url: "/region",
            type: 'POST',  // http method
            data: {
                keyword1: document.getElementById('keyword1').value,
                keyword2:document.getElementById('keyword2').value,
                resolution: 'DMA',
                largest_region_len: 10
             },  // data to submit
            success: function (data) {
                console.log(data, '88888')
                if(!data.error) {
                   get_regions();
                }
            },
            error: function (jqXhr, textStatus, errorMessage) {
                    alert(errorMessage);
            }
        });
}

     // validate user added keywords
$(".validate").on("click", function () {
    if (!valid()) {
        alert("Please, provide valid keywords.");
        return false;
    }
});

function valid() {
    let keyword1 = document.getElementById('keyword1').value;
    let keyword2 = document.getElementById('keyword2').value;
    return keyword1 && keyword2 ? true : false;
}



function get_regions() {
var kw1 = document.getElementById('keyword1').value;
var kw2 = document.getElementById('keyword2').value;
$.ajax({
    type: "GET",
    url: `/regions/${kw1}/${kw2}`,
    data: {},
    success: function(data) {
        if(!data.success) {
            document.getElementById('keyword1').value = "";
            document.getElementById('keyword2').value = "";
            alert(data.msg)
        }
        else {
            document.getElementById('keyword1').value = data.keyword1;
            document.getElementById('keyword2').value = data.keyword2;
            draw_heat_map(data)
        }
    }
});
}

function draw_heat_map(data) {
var regions_data = data;
    am5.ready(function() {
    // Create root element
    // https://www.amcharts.com/docs/v5/getting-started/#Root_element
    var root = am5.Root.new("chartdiv");


    // Set themes
    // https://www.amcharts.com/docs/v5/concepts/themes/
    root.setThemes([
      am5themes_Animated.new(root)
    ]);


    // Create chart
    // https://www.amcharts.com/docs/v5/charts/xy-chart/
    var chart = root.container.children.push(am5xy.XYChart.new(root, {
      panX: false,
      panY: false,
      wheelX: "none",
      wheelY: "none",
      layout: root.verticalLayout
    }));


    // Create axes and their renderers
    var yRenderer = am5xy.AxisRendererY.new(root, {
      visible: false,
      minGridDistance: 20,
      inversed: true
    });

    yRenderer.grid.template.set("visible", false);

    var yAxis = chart.yAxes.push(am5xy.CategoryAxis.new(root, {
      maxDeviation: 0,
      renderer: yRenderer,
      categoryField: "region"
    }));

    var xRenderer = am5xy.AxisRendererX.new(root, {
      visible: false,
      minGridDistance: 30,
      opposite:true
    });

    xRenderer.grid.template.set("visible", false);

    var xAxis = chart.xAxes.push(am5xy.CategoryAxis.new(root, {
      renderer: xRenderer,
      categoryField: "trends"
    }));


    // Create series
    // https://www.amcharts.com/docs/v5/charts/xy-chart/#Adding_series
    var series = chart.series.push(am5xy.ColumnSeries.new(root, {
      calculateAggregates: true,
      stroke: am5.color(0xffffff),
      clustered: false,
      xAxis: xAxis,
      yAxis: yAxis,
      categoryXField: "trends",
      categoryYField: "region",
      valueField: "trends"
    }));

    series.columns.template.setAll({
      tooltipText: "{value}",
      strokeOpacity: 1,
      strokeWidth: 2,
      width: am5.percent(100),
      height: am5.percent(100)
    });

    series.columns.template.events.on("pointerover", function(event) {
      var di = event.target.dataItem;
      if (di) {
        heatLegend.showValue(di.get("value", 0));
      }
    });

    series.events.on("datavalidated", function() {
      heatLegend.set("startValue", series.getPrivate("valueHigh"));
      heatLegend.set("endValue", series.getPrivate("valueLow"));
    });


    // Set up heat rules
    // https://www.amcharts.com/docs/v5/concepts/settings/heat-rules/
    series.set("heatRules", [{
      target: series.columns.template,
      min: am5.color(0xfffb77),
      max: am5.color(0xfe131a),
      dataField: "value",
      key: "fill"
    }]);


    // Add heat legend
    // https://www.amcharts.com/docs/v5/concepts/legend/heat-legend/
    var heatLegend = chart.bottomAxesContainer.children.push(am5.HeatLegend.new(root, {
      orientation: "horizontal",
      endColor: am5.color(0xfffb77),
      startColor: am5.color(0xfe131a)
    }));


    // Set data
    // https://www.amcharts.com/docs/v5/charts/xy-chart/#Setting_data
    var data = regions_data.regions;

    series.data.setAll(data);

    yAxis.data.setAll(regions_data.regions_list);

    xAxis.data.setAll(regions_data.trends_list);

    // Make stuff animate on load
    // https://www.amcharts.com/docs/v5/concepts/animations/#Initial_animation
    chart.appear(1000, 100);

    }); // end am5.ready()
}
