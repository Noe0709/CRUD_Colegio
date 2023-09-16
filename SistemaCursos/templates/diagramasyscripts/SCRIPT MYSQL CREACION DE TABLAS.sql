CREATE TABLE `Profesores` (
  `id_profesor` int,
  `nombre_p` varchar(50),
  `edad_p` int,
  `materia` varchar(50),
  `años_experiencia` int,
  PRIMARY KEY (`id_profesor`)
);

CREATE TABLE `Estudiantes` (
  `id_estudiante` int,
  `nombre_e` varchar(50),
  `edad_e` int,
  `grado` varchar(75),
  `promedio` float,
  PRIMARY KEY (`id_estudiante`)
);

CREATE TABLE `Cursos` (
  `id_curso` int,
  `nombre_curso` varchar(75),
  `nivel` varchar(35),
  `capacidad` int,
  `horario` timestamp,
  `id_profesor` int,
  `id_estudiante` int,
  PRIMARY KEY (`id_curso`),
  FOREIGN KEY (`id_profesor`) REFERENCES `Profesores`(`id_profesor`),
  FOREIGN KEY (`id_estudiante`) REFERENCES `Estudiantes`(`id_estudiante`)
);