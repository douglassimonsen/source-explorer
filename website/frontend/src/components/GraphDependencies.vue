<template>
  <div id="graph"></div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import axios from 'axios';
import cytoscape from 'cytoscape';
import dagre from 'cytoscape-dagre';
cytoscape.use( dagre );
const COLORS = {
  'VIEW': 'green',
  'BASE TABLE': 'blue'
};
@Options({
  props: {
  },
})
export default class HelloWorld extends Vue {
  mounted () {
   axios.get('http://127.0.0.1:5000/api/views/redshift', {headers: {'Access-Control-Allow-Origin': '*'}}).then(function(resp){
    const nodes = resp.data.objects.map(function(x){
      return {
        data: {
          id: `${x.table_schema}.${x.table_name}`,
          name: `${x.table_schema}.${x.table_name}`,
          color: COLORS[x.table_type],
        },
      };
    });
    const edges = resp.data.dependencies.map(function(x){
      return {
        data: {
          id: `${x.parent_schema}.${x.parent_table}-${x.child_schema}.${x.child_view}`,
          source: `${x.parent_schema}.${x.parent_table}`,
          target: `${x.child_schema}.${x.child_view}`,
        }
      }
    });
    cytoscape({
      container: document.getElementById("graph"),
      elements: nodes.concat(edges),
      layout: {
        name: 'dagre',
      },
      style: [
        {
          selector: 'node',
          style: {
            shape: 'rectangle',
            'background-color': 'data(color)',
            label: 'data(id)',
          },
        },
      ],
    });    
   })
    
  }
}
</script>

<style scoped>
#graph {
    width: 400px;
    height: 400px;
    position: absolute;
    background-color: aqua;
    top: 0px;
    left: 0px;
}
</style>
