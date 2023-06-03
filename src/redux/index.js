import { createSlice } from '@reduxjs/toolkit'

export const incdecSlice = createSlice({
    name: 'indec',
    initialState: 0,
    reducers: {
      inc: (state, action) => {
        return state +=1
      },
      dec: (state, action) => {
        return state -=1
      }
    },
  })

export const { inc, dec } = incdecSlice.actions;

export default incdecSlice.reducer;