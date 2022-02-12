<template>
  <div id="graph"></div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import axios from 'axios';
import cytoscape from 'cytoscape';
import dagre from 'cytoscape-dagre';
cytoscape.use( dagre );

@Options({
  props: {
  },
})
export default class HelloWorld extends Vue {
  mounted () {
   axios.get('http://127.0.0.1:5000/api/views/redshift', {headers: {'Access-Control-Allow-Origin': '*'}}).then(function(resp){
    debugger;     
   })
    cytoscape({
      // eslint-disable-next-line  @typescript-eslint/no-explicit-any
      container: document.getElementById("graph"),
      elements: [
        { data: { id: 'a' } },
        { data: { id: 'b' } },
        {
          data: {
            id: 'ab',
            source: 'a',
            target: 'b'
          }
        }
      ],
    });
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
