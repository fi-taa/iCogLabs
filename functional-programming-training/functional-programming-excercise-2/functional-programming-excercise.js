const { produce } = require('immer');

{/*
    you should use a function called EventReducer, that takes the “dataStore” as an argument and
    returns the updated dataStore. The EventReducer also takes an “event” as an argument. 
    An event is just a plain javascript object that describes what just happened, 
    such as, item added to cart, user logged in, etc. Based on the type of the event
    the EventReducer should know which properties of the object it should update.
    Your task is to define the EventReducer, a user will then use to update the dateStore.

  */}

// Event reducer with immer to implement immutability
const EventReducer = (dataStore, event) => {
  return produce(dataStore, draft => {
    switch (event.type) {
      case 'addItem':
        draft.items.push(event.payload);
        break;
      case 'loginUser':
        draft.user = event.payload;
        break;
      default:
        break;
    }
  });
};
{/*

 You should also create a “dispatchEvent” method that takes an
 “event” object and forwards it to the EventReducer to be processed. 
 Then the EventReducer should compute the new dataStore and return it.
  
  */}

// Dispatch event function
const dispatchEvent = (history, currentStateIndex) => (event) => (dataStore) => {
  logActions("Event dispatched: ")(event); // Log the event
  const newState = EventReducer(dataStore, event);
  return curriedRecordState(history)(currentStateIndex)(newState);
};

{/*
  You should also implement a “logActions” curried function 
  that helps to log to the console every time an event is dispatched.
  
  */}
// Log actions function
const logActions = (msg) => (event) => {
  console.log(msg, event);
  return event;
};


{/*
  
  You should also implement an “undoAction” and “redoAction”
   curried functions that helps to undo and redo 
   the last change made to the dataStore respectively. 
   It should only change the dataStore if an event was 
   undone or the  “undoAction” function was run before it.
  
  */}
const curriedUndoAction = (history) => (currentStateIndex) => (dataStore) => {
  if (currentStateIndex > 0) {
    const newStateIndex = currentStateIndex - 1;
    return { newState: history[newStateIndex], newStateIndex };
  }
  return { newState: dataStore, newStateIndex: currentStateIndex };
};

const curriedRedoAction = (history) => (currentStateIndex) => (dataStore) => {
  if (currentStateIndex < history.length - 1) {
    const newStateIndex = currentStateIndex + 1;
    return { newState: history[newStateIndex], newStateIndex };
  }
  return { newState: dataStore, newStateIndex: currentStateIndex };
};

// Record state function to keep track of the history
const curriedRecordState = (history) => (currentStateIndex) => (newState) => {
  const newHistory = history.slice(0, currentStateIndex + 1).concat(newState);
  const newStateIndex = currentStateIndex + 1;
  return { newHistory, newStateIndex };
};

let dataStore = { items: [], user: null };
let history = [];
let currentStateIndex = -1;

// Initialize the state
({ newHistory: history, newStateIndex: currentStateIndex } = curriedRecordState(history)(currentStateIndex)(dataStore));

// Dispatch addItem event
({ newHistory: history, newStateIndex: currentStateIndex } = dispatchEvent(history, currentStateIndex)({ type: 'addItem', payload: { id: 1, name: 'Item 1' } })(dataStore));
dataStore = history[currentStateIndex]; // Update dataStore to the new state

// Dispatch loginUser event
({ newHistory: history, newStateIndex: currentStateIndex } = dispatchEvent(history, currentStateIndex)({ type: 'loginUser', payload: { username: 'user1', role: 'admin' } })(dataStore));
dataStore = history[currentStateIndex]; // Update dataStore to the new state

console.log('Initial state:', dataStore, currentStateIndex);

// Record a new state
({ newHistory: history, newStateIndex: currentStateIndex } = curriedRecordState(history)(currentStateIndex)({ items: ["Item 2"], user: "staff" }));
dataStore = history[currentStateIndex];
console.log('State after first change:', dataStore, currentStateIndex);

// Perform undo
({ newState: dataStore, newStateIndex: currentStateIndex } = curriedUndoAction(history)(currentStateIndex)(dataStore));
console.log('State after undo:', dataStore, currentStateIndex);

// Perform redo
({ newState: dataStore, newStateIndex: currentStateIndex } = curriedRedoAction(history)(currentStateIndex)(dataStore));
console.log('State after redo:', dataStore, currentStateIndex);

