import * as types from "../Constants/action.names";

export function setCurrentTab(state = "deligate", action) {
    switch (action.type) {
        case types.CURRENT_TAB:
            return action.payload;
        default:
            return state;
    }
}
