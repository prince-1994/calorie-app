import snakeize from 'snakeize'
import camelize from 'camelize'

export default (ctx, inject) => {
    const utils = {
        snakeize,
        camelize,
      }
      inject('commonUtils', utils)
}