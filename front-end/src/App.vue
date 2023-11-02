<template>
  <!-- HTML for your component -->
  <div>
    {{ message }}
  </div>
</template>

<script>
// This is where your JavaScript goes
import axios from 'axios';
export default {
  data() {
    return {
      message: ''
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      // Assuming you have axios available globally or imported in the script
      axios.get('http://localhost:5000/api/data')
    .then(response => {
        // handle success
        console.log(response.data);
    })
    .catch(error => {
        // handle error
        console.log(error);
    });

      }
}
}
</script>

<style>
/* CSS specific to this component */
</style>

