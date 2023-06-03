import React, { useMemo } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { inc, dec } from '../redux/index';

export function Counter() {
  const count = useSelector((state) => state.indec);
  const dispatch = useDispatch();

  const memoizedCount = useMemo(() => count, [count]);

  const handleIncrement = () => {
    dispatch(inc());
  };

  const handleDecrement = () => {
    dispatch(dec());
  };

  return (
    <div>
      <div>
        <button
          aria-label="Increment value"
          onClick={handleIncrement}
        >
          Increment
        </button>
        <span>{memoizedCount}</span>
        <button
          aria-label="Decrement value"
          onClick={handleDecrement}
        >
          Decrement
        </button>
      </div>
    </div>
  );
}
