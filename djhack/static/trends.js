    var dataset  = [],
    menArray  = [],
    womenArray = [],
    menObjectArray = [],
    womenObjectArray = [],
    stack = d3.layout.stack(),
  menRow = d3.selectAll("tr.men"),
    womenRow = d3.selectAll("tr.women"),
    /*Width and height*/
    w = 630,
    h = 200,
    barPadding = 5,
    padding = 60
  duration = 500,
  grouped = false;


    // menRow.each(function() {
    //     d3.select(this).selectAll("td").each(function() {
    //         menArray.push(parseInt(d3.select(this).text()));
    //     })
    // });

    // womenRow.each(function() {
    //     d3.select(this).selectAll("td").each(function() {
    //         womenArray.push(parseInt(d3.select(this).text()));
    //     })
    // });
    menArray=[12,23,45,63,32,43,34]     //resolved
    womenArray=[11,6,43,23,43,21,10]    //pending
    for (var i = 0; i < menArray.length; i++) {
        var newObject = {};
        newObject.x = i;
        newObject.y = menArray[i];
        menObjectArray.push(newObject);
    };

    for (var i = 0; i < womenArray.length; i++) {
        var newObject = {};
        newObject.x = i;
        newObject.y = womenArray[i];
        womenObjectArray.push(newObject);
    };

    dataset.push(menObjectArray);
    dataset.push(womenObjectArray);
    console.log(dataset);
    stack(dataset);

    /* Define Y scale */
    var yScale = d3.scale.linear()
        .domain([0,
            d3.max(dataset, function(d) {
                return d3.max(d, function(d) {
                    return d.y0 + d.y;
                });
            })
        ])
        .range([h, padding]);

    /* Create SVG element */
    var svg = d3.select(".info-chart")
        .append("svg")
        .attr("width", w)
        .attr("height", h);

    /* Add a group for each row of data */
    var groups = svg.selectAll("g")
        .data(dataset)
        .enter()
        .append("g")
        .style("fill", function(d, i) {
            return  i === 0 ? "#11AA22" : "#E53524";
        });

    groups.selectAll("rect")
        .data(function(d) { return d; })
        .enter()
        .append("rect")
        .attr("x", function(d, i){
            return i * (w / dataset[0].length);
        })
        .attr("y", function(d){
            return yScale(d.y) + yScale(d.y0) - h;
        })
        .attr("width", w / dataset[0].length - barPadding )
        .attr("height", function(d){
            return h - yScale(d.y);
        })
        .on("mouseover", function(d) {

            /* Get this bar's x/y values, then augment for the tooltip */
            var xPosition,
            yPosition = parseInt(d3.select(this).attr("y") );


            if (d3.select(this).attr("x") < 350) {

        if (grouped) {
            console.log("We be grouped!");
            xPosition = parseFloat(d3.select(this).attr("x")) + 14;
          } else  {
            xPosition = parseFloat(d3.select(this).attr("x")) + 27;
          }

                d3.select(".tooltip").classed("tooltip-left", false).classed("tooltip-right", true);
            } else {
                xPosition = parseFloat(d3.select(this).attr("x")) - 27;
                d3.select(".tooltip").classed("tooltip-left", true).classed("tooltip-right", false);;
            }

            /* Update the tooltip position and value */
            d3.select(".tooltip")
                .style("left", xPosition + "px")
                .style("top", yPosition + "px")
                .select(".value")
                .text(d.y);

            /* Show the tooltip */
            d3.select(".tooltip").classed("hidden", false);

            })
            .on("mouseout", function() {
                /* Hide the tooltip */
                d3.select(".tooltip").classed("hidden", true);
            });

d3.selectAll("input").on("change", change);

function change() {
  if (this.value === "grouped") {
    grouped = true;
    transitionGrouped();
  } else  {
    grouped = false;
    transitionStacked();
  }
}

var transitionGrouped = function() {
    groups.selectAll("rect")
        .transition()
        .duration(duration)
    .delay(function(d, i) { return i / dataset[0].length * duration; })
        .attr("width", (w / dataset[0].length - barPadding) / 2 )
        .transition()
        .duration(duration)
        .attr("x", function(d, i, j){
            return i * (w / dataset[0].length) + ((w / dataset[0].length - barPadding)/2) * j ;
        })
        .transition()
    .duration(duration)
        .attr("y", function(d, i, j){
            return yScale(d.y);
        });
};

var transitionStacked = function() {
    groups.selectAll("rect")
        .transition()
    .duration(duration)
    .delay(function(d, i) { return i / dataset[0].length * duration; })
        .attr("y", function(d){
            return yScale(d.y) + yScale(d.y0) - h;
        })
        .transition()
        .duration(duration)
        .attr("x", function(d, i){
            return i * (w / dataset[0].length);
        })
        .transition()
        .duration(duration)
        .attr("width", w / dataset[0].length - barPadding );
};
