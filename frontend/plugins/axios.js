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
  const handleBadRequestError = (error) => {
    const data = error.response.data
    if (data.constructor !== Object) {
      return
    }
    for (const key in data) {
      for (const str of data[key]) {
        store.dispatch('addTemporaryMessage', {
          message: `${key} : ${str}`,
          type: 'error',
        })
      }
    }
  }

  $axios.onError((error) => {
    if (error.response.status === 500) {
      store.dispatch('addTemporaryMessage', {
        message: 'Something went wrong. We are sorry.',
        type: 'error',
      })
    } else if (
      error.response.status === 401 &&
      error.request.config.url !== '/api/userprofiles/profiles/'
    ) {
      store.dispatch('addTemporaryMessage', {
        message: 'You are unauthorized to perform this action.',
        type: 'error',
      })
    } else if (error.response.status === 400) {
      handleBadRequestError(error)
    }
  })
}
