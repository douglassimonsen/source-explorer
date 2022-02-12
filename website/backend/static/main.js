const COLORS = {
  
}
new Vue({
  el: '#main',
  data: function(){
    return {};
  },
  mounted: function(){
    axios.get('/api/views/redshift').then(function(resp){
      nodes = resp.data.map(function(x){
        return [
          {data: {id: `${x.child_schema}.${x.child_view}`}},
          {data: {id: `${x.parent_schema}.${x.parent_table}`}},
        ]
      }).flat();
      edges = resp.data.map(function(x){
        return {data: {
          id: `${x.child_schema}.${x.child_view}-${x.parent_schema}.${x.parent_table}`,
          source: `${x.parent_schema}.${x.parent_table}`,
          target: `${x.child_schema}.${x.child_view}`,
        }}
      })
      cytoscape({
        elements: nodes.concat(edges), 
        container: document.getElementById("graph")
      });
    }.bind(this));
  }
})