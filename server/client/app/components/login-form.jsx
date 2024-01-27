import formStyles from "./form.module.css";

export default function LoginForm() {
  return (
    <form className={formStyles.form}>
      <label htmlFor="email">
        Email: <input type="text" id="email" />
      </label>
      <label htmlFor="password">
        Password: <input type="text" id="password" />
      </label>
      <button type="submit">Log In</button>
      Or
      <button>Sign Up</button>
    </form>
  );
}
