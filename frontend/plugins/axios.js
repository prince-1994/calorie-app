export default function ({ $axios, $commonUtils, store }) {
    store.commit('initialize')
    $axios.setToken(store.state.token, 'Token')
    $axios.onRequest((config) => {
      config.data = $commonUtils.snakeize(config.data)
      return config
    })
  
    $axios.onResponse((response) => {
      response.data = $commonUtils.camelize(response.data)
      return response
    })
  }
  