/*
 *
 * HomePage actions
 *
 */

import {
  TODO_CREATING,
  TODOS_FETCHING,
  TODO_DELETING,
} from './constants';

export function createTodo() {
  console.log('%c createTodo Action', 'color: green');
  return {
    type: TODO_CREATING,
  };
}

export function fetchTodos() {
  console.log('%c fetchTodos Action', 'color: green');
  return {
    type: TODOS_FETCHING,
  };
}

export function deleteTodo(id) {
  console.log('%c deleteTodo Action', 'color: green');
  return {
    type: TODO_DELETING,
    payload: id,
  };
}
