import PromptForm from "@/components/prompt/prompt.component";
import Sidebar from "@/components/sidebar/sidebar.component";
import Image from "next/image";

export default function Home() {
  return (
    <div className="w-100 m-5">
      <Sidebar />
      <article className="">
        <PromptForm />
      </article>
    </div>
  );
}
