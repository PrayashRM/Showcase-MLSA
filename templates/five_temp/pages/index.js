import AboutContainer from "../../Components/AboutContainer";
import ContactContainer from "../../Components/ContactContainer";
import InitialContainer from "../../Components/InitialContainer";
import KnowledgeContainer from "../../Components/KnowledgeContainer";
import ProjectsContainer from "../../Components/ProjectsContainer";

export default function Home() {
  return (
    <>
      <InitialContainer />
      <AboutContainer />
      <ProjectsContainer />
      <KnowledgeContainer />
      <ContactContainer />
    </>
  )
}
