import { createSlice } from '@reduxjs/toolkit';

// Define your initial state
const initialState = {
  co: 0,
};

// Define a slice for the counter state
const counterSlice = createSlice({
  name: 'counter',
  initialState,
  reducers: {
    increment: (state) => {
      state.co += 1;
    },
    decrement: (state) => {
      state.co -= 1;
    },
  },
});

export const { increment, decrement } = counterSlice.actions;

export default counterSlice.reducer;
