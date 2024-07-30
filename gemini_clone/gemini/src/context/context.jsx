import { createContext } from "react";

export const Context = createContext();


const ContextProvider = (props) => {

    const onsent = async(prompt) => {
        runchat(prompt)

    }

    onsent()

    const contextValue = {


    }
    return (
        <Context.Provider value={contextValue}>
            {props.children}
        </Context.Provider>
    )
}


export default ContextProvider