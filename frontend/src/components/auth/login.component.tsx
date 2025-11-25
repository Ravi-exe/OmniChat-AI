"use client";
import { Button, Checkbox, FormControl, TextField } from "@mui/material"

export default function LoginComponent() {


    return (
        <form className="LoginForm">
            
            <TextField inputMode="email" placeholder="Enter your Email" />
            <TextField inputMode="text"  placeholder="Enter your password"/>
            <Button>Submit</Button>

            {/* <Checkbox />Login with OTP */}
        </form>
    )
}
