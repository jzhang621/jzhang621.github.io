var margin = {top: 20, right: 20, bottom: 20, left: 20},
    width = 400 - margin.left - margin.right,
    height = 100 - margin.top - margin.bottom;


/*
 * Initialize the d3 progress bar object
 */
function initBar(name) {
  var svg = d3.select(".progress-section").append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("width", 400)
      .attr("height", 200)
    .append("rect")
      .attr("width", 400)
      .attr("height", 200)
      .attr("fill", "cadetblue");

};

/*
 * Draw the progress as given by the parameter.
 */
function drawBar(progress) {

};
