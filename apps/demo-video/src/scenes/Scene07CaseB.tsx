import React from 'react';
import { interpolate, useCurrentFrame } from 'remotion';
import { theme } from '../theme';
import { PhoneCard } from '../components/PhoneCard';
import { DecisionBadge } from '../components/DecisionBadge';
import simulationData from '../data/simulation.json';

export const Scene07CaseB: React.FC = () => {
  const frame = useCurrentFrame();
  const caseB = simulationData.case_b;

  const phoneX = interpolate(frame, [0, 30], [-100, 0], { extrapolateRight: 'clamp' });
  const phoneOpacity = interpolate(frame, [0, 30], [0, 1], { extrapolateRight: 'clamp' });

  // Typewriter effect for the warning message (starts around frame 120)
  const messageChars = Math.floor(interpolate(frame, [100, 240], [0, caseB.payer_message_es.length], { extrapolateRight: 'clamp' }));

  // Cancellation happens around frame 350
  const isCancelled = frame > 380;

  return (
    <div
      style={{
        flex: 1,
        backgroundColor: theme.colors.bg,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '0 80px',
        gap: '60px',
      }}
    >
      {/* Phone container */}
      <div
        style={{
          opacity: phoneOpacity,
          transform: `translateX(${phoneX}px)`,
        }}
      >
        <PhoneCard
          amount={caseB.amount}
          recipientClabe={caseB.destination_clabe}
          recipientBank="STP"
          payerMessage={caseB.payer_message_es}
          visibleChars={messageChars}
          isCancelled={isCancelled}
        />
      </div>

      {/* Incident Details / Sentinel Analysis */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '14px', marginBottom: '14px' }}>
          <DecisionBadge decision="pause" size="lg" />
          <span style={{ color: '#ef4444', fontFamily: theme.fonts.mono, fontSize: '16px', fontWeight: 700 }}>
            INTERVENCIÓN ACTIVA (DÍA 3)
          </span>
        </div>

        <h2 style={{ color: '#fff', fontFamily: theme.fonts.serif, fontSize: '42px', margin: '0 0 20px 0', lineHeight: 1.15 }}>
          Ataque de Ingeniería Social Interceptado
        </h2>

        {/* Signals List */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginBottom: '30px' }}>
          <div style={{ backgroundColor: theme.colors.surface, border: '1px solid #ef4444', borderRadius: '10px', padding: '14px 18px', display: 'flex', justifyContent: 'space-between' }}>
            <span style={{ color: '#fff' }}>1. Beneficiario nuevo (alta &lt; 15 min)</span>
            <span style={{ color: '#ef4444', fontFamily: theme.fonts.mono, fontWeight: 700 }}>RECEPTOR</span>
          </div>
          <div style={{ backgroundColor: theme.colors.surface, border: '1px solid #ef4444', borderRadius: '10px', padding: '14px 18px', display: 'flex', justifyContent: 'space-between' }}>
            <span style={{ color: '#fff' }}>2. Monto estructurado ($12,450 debajo de umbral)</span>
            <span style={{ color: '#ef4444', fontFamily: theme.fonts.mono, fontWeight: 700 }}>INTENCIÓN</span>
          </div>
          <div style={{ backgroundColor: theme.colors.surface, border: '1px solid #ef4444', borderRadius: '10px', padding: '14px 18px', display: 'flex', justifyContent: 'space-between' }}>
            <span style={{ color: '#fff' }}>3. Llamada telefónica activa durante la sesión</span>
            <span style={{ color: '#ef4444', fontFamily: theme.fonts.mono, fontWeight: 700 }}>SESIÓN</span>
          </div>
        </div>

        {/* Impact Box */}
        <div
          style={{
            backgroundColor: isCancelled ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)',
            border: `1.5px solid ${isCancelled ? theme.colors.allow : theme.colors.pause}`,
            borderRadius: '12px',
            padding: '20px 24px',
            transition: 'all 0.3s ease',
          }}
        >
          <div style={{ color: theme.colors.textMuted, fontSize: '13px', fontFamily: theme.fonts.mono, textTransform: 'uppercase' }}>
            RESULTADO DE LA FRICCIÓN
          </div>
          <div style={{ color: isCancelled ? theme.colors.allow : '#fff', fontSize: '30px', fontFamily: theme.fonts.mono, fontWeight: 700, marginTop: '4px' }}>
            {isCancelled ? '$12,450.00 MXN PROTEGIDOS' : 'Evaluando respuesta del usuario...'}
          </div>
          <div style={{ color: theme.colors.textSecondary, fontSize: '14px', marginTop: '6px' }}>
            {isCancelled ? 'El usuario leyó la advertencia, reconoció el intento de engaño y canceló.' : 'Pausa preventiva antes de enviar orden a Banxico.'}
          </div>
        </div>
      </div>
    </div>
  );
};
