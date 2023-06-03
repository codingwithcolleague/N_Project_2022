import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { increment, decrement } from './reducers';

const Counter = () => {
  const dispatch = useDispatch();
  const counter = useSelector((state) => state.co);

  return (
    <div>
      <h2>Counter: {counter}</h2>
      <button onClick={() => dispatch(increment())}>Increment</button>
      <button onClick={() => dispatch(decrement())}>Decrement</button>
    </div>
  );
};

export default Counter;
