<script >
import axios from "axios"

let searchValue = ''
console.log(searchValue)

export default ({
  data() {
    return {
      dados: [], //objeto que armazena os dados do banco 
      searchValue: ''
    }
  },
  computed: {

  },
  methods: {
    async filtrar(input) {
      console.log(`.${input}.`)
      if (input == '') {
        try {
          const config = {
            method: 'get',
            url: `http://localhost:8000/`
          }
          const response = await axios(config);
          this.dados = response.data
          console.log(response)
        } catch (error) {
          console.error(error);
        }
      } else {
        try {
          const config = {
            method: 'get',
            url: `http://localhost:8000/buscar/${input}`
          }
          const response = await axios(config);
          this.dados = response.data
          console.log(response)
        } catch (error) {
          console.error(error);
        }
      }
    }
  }
})

</script>

<template>
  <container class="container">
    <h1>Operadoras Ativas</h1>
    <div class="form">
      <input placeholder="Pesquise aqui a operadora" v-model="searchValue" />
        <button type="submit" v-on:click="filtrar(searchValue)">Pesquisar</button>
    </div>
    <div class="container_table">
      <table>
        <tr class="titulo_table">
          <th>Data</th>
          <th>Razao Social</th>
          <th>CNPJ</th>
          <th>Representante</th>
          <th>Email</th>
        </tr>
        <tr v-for="dado in dados" :key="dado.cnpj">
          <td>{{ dado.data_registro }}</td>
          <td>{{ dado.razao_social }}</td>
          <td>{{ dado.cnpj }}</td>
          <td>{{ dado.representante }}</td>
          <td>{{ dado.endereco }}</td>
        </tr>
      </table>
    </div>
  </container>
</template>

<style scoped>
h1 {
  margin-left: 1rem;
  color: #5d8aa8;
}

.container {
  color: #bdbebd;
  width: 75rem;
  background-color: #111111;
  border-radius: 1rem;
  padding: 0.5rem;
  margin: 3rem auto;
  display: flex;
  flex-direction: column;
  justify-content: start;
}

.container,
.form {
  margin: 0 auto;
  margin-bottom: 2rem;
}


div button {
  padding: 0.3rem;
  border-radius: 8px;
  margin-left: 1rem;
  background-color: #084d6e;
  color: #bdbebd;
  border: none;
  margin-left: 2.5rem;
}

div button:hover {
  cursor: pointer;
  padding: 0.4rem;
  color: aliceblue;
}

input {
  background-color: black;
  color: #bdbebd;
  border: none;
  border-radius: 8px;
  width: 62rem;
  height: 20px;
  padding: 0.5rem;
  margin-left: -2rem;
  line-height: 20px;
}

.container_table {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

table {
  list-style: none;
  border: 1px #bdbebd solid;
  border-radius: 6px;
  width: 75rem;
}

table>tr>.titulo_table {
  word-break: break-word;
  height: 3rem;
  font-size: small;
  border: 6px solid 1px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

table>tr>th {
  width: 240;
  border: 6px solid 1px;
  padding: 0.7rem;

}


table>tr>td {
  width: 240;
  border: 6px solid 1px;
  padding: 0.7rem;

}
</style>
