import api from "../api/axiosConfig";


interface LoginData {
    username:string;
    password:string;
}


export const login = async(data:LoginData)=>{

    const response = await api.post(
        "/auth/login",
        data
    );


    return response.data;

};